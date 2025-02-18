from autogen import ConversableAgent, AssistantAgent, Agent
from autogen.coding import LocalCommandLineCodeExecutor
from app.config import settings
from typing import Dict, Optional

def should_terminate(msg: Dict) -> bool:
    """
    Determine if the conversation should terminate.
    """
    if isinstance(msg.get("content"), str):
        return "TERMINATE" in msg.get("content").upper()
    return False

def create_executor(timeout: int = 60):
    """
    Create a code executor for the agents.
    
    Args:
        timeout (int): Maximum execution time in seconds
    
    Returns:
        LocalCommandLineCodeExecutor: Configured code executor
    """
    return LocalCommandLineCodeExecutor(
        timeout=timeout,
        work_dir="coding"
    )

def create_code_executor_agent(
    name: str = "code_executor_agent",
    human_input_mode: str = "NEVER"
) -> ConversableAgent:
    """
    Create an agent with code execution capabilities.
    
    Args:
        name (str): Name of the agent
        human_input_mode (str): Mode for human input ('NEVER', 'TERMINATE', 'ALWAYS')
    
    Returns:
        ConversableAgent: Configured executor agent
    """
    executor = create_executor()
    
    # Define termination messages
    termination_msg = "Task completed successfully. TERMINATE"
    
    agent = ConversableAgent(
        name=name,
        llm_config=False,
        code_execution_config={"executor": executor},
        human_input_mode=human_input_mode,
        default_auto_reply=None,  # Don't auto-reply
        max_consecutive_auto_reply=3,  # Limit consecutive auto-replies
        is_termination_msg=should_terminate,  # Custom termination check
        system_message="""I am a code executor agent. I will:
1. Execute code provided by the code writer
2. Report results and any errors
3. Terminate when the task is complete
4. Reply with 'TERMINATE' when finished"""
    )
    
    return agent

def create_code_writer_agent(
    name: str = "code_writer_agent",
    model: Optional[str] = None
) -> AssistantAgent:
    """
    Create an agent with code writing capabilities.
    
    Args:
        name (str): Name of the agent
        model (str, optional): OpenAI model to use
    
    Returns:
        AssistantAgent: Configured writer agent
    """
    llm_config = {
        "model": model or settings.OPENAI_MODEL,
        "api_key": settings.OPENAI_API_KEY,
        "temperature": 0.7,
        "config_list": [{
            "model": model or settings.OPENAI_MODEL,
            "api_key": settings.OPENAI_API_KEY,
        }]
    }
    
    agent = AssistantAgent(
        name=name,
        llm_config=llm_config,
        code_execution_config=False,
        human_input_mode="NEVER",
        system_message="""I am a code writer agent. I will:
1. Write clear, efficient Python code
2. Put code in markdown code blocks
3. Ensure code is complete and ready to execute
4. Respond to feedback from the executor agent
5. Signal completion with 'TERMINATE'"""
    )
    
    return agent

# Create instances of the agents with improved termination handling
code_executor_agent = create_code_executor_agent()
code_writer_agent = create_code_writer_agent() 
import importlib


DEFAULT_VERSION="v1"

def load_agent_prompts(version):
    module = importlib.import_module(f"prompts.{version}.agents")
    return {
        "research":module.RESEARCH_AGENT,
        "writer":module.WRITER_AGENT,
        "validator":module.VALIDATOR_AGENT,
    }
    
def load_task_prompts(version):
    module=importlib.import_module(f"prompts.{version}.tasks")
    return {
        "research":module.RESEARCH_TASK,
        "writer":module.WRITER_TASK,
        "validator":module.VALIDATION_TASK,
    }
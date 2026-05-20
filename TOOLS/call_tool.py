from LLM.llm import llm
from TOOLS.registry import TOOL_MAP
import json


def call_tool(tool):
    name =tool.function.name
    args = json.loads(tool.function.arguments)
    func = TOOL_MAP.get(name)

    if func is None:
        return "unknown tool was asked to call"
    else:
        try:
            result = str(func(**args))
        except Exception as e:
            result = f"Error: {e}"
    return result
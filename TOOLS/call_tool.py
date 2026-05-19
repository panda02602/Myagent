from LLM.llm import llm
from TOOLS.registry import TOOL_MAP
import json

def call_tool(tool, context: list):  # ✅ Receives a single tool call, not full message
    name = tool.function.name
    args = json.loads(tool.function.arguments)
    func = TOOL_MAP.get(name)

    if func is None:
        return "unknown tool was asked to call"
    try:
        return str(func(**args))
    except Exception as e:
        return f"Error: {e}"
from INTELLIGENCE_LAYER.intelligence import IntelligenceLayer
from CONTEXT_LAYER.context_manager import ContextLayer
from TOOLS.call_tool import call_tool
import json

class Agent:
    def __init__(self):
        self.intelligence_layer = IntelligenceLayer()
        self.context_layer = ContextLayer()

    def set_sys_prompt(self, _sys_PROMPT):
        self.context_layer.get_sys_prompt(_sys_PROMPT)

    def step(self, prompt: str):
        self.context_layer.build_context(prompt)
        response_text = ""

        while True:
            response = self.intelligence_layer.process(self.context_layer.get_context())
            message = response.choices[0].message  # ✅ chat.completions structure

            # Append assistant message to context
            self.context_layer.extend([message])

            if message.tool_calls:  # ✅ Tool call check for chat.completions
                for tool in message.tool_calls:
                    tool_result = call_tool(tool, self.context_layer.get_context())

                    self.context_layer.extend([
                        {
                            "role": "tool",
                            "tool_call_id": tool.id,
                            "name": tool.function.name,
                            "content": str(tool_result)
                        }
                    ])
                # Loop again to get final response after tool use

            else:
                response_text = message.content  # ✅ Plain text response
                break

        return response_text
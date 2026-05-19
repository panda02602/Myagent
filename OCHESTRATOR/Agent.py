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
            message = response.choices[0].message

            if message.tool_calls:
                # Append assistant's tool call request to context
                self.context_layer.extend([message])

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
                # Loop again to get the final response after tool execution

            elif hasattr(message, "reasoning_content") and message.reasoning_content:
                # Reasoning message — append and continue
                reasoning_text = message.reasoning_content
                self.context_layer.extend([
                    {
                        "role": "assistant",
                        "content": reasoning_text
                    }
                ])
                response_text = reasoning_text
                break

            else:
                # Normal text message — append to context and return
                response_text = message.content or ""
                self.context_layer.extend([
                    {
                        "role": "assistant",
                        "content": response_text
                    }
                ])
                break

        return response_text
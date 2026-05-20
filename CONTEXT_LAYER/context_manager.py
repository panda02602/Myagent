from openai.types.responses.response_output_item import ResponseOutputItem
class ContextLayer:
    def __init__(self) -> None:
        self._sys_PROMPT = ""
        self._context: list = [{'role': 'system', 'content': "you're a good assistant"}]

    def get_context(self):
        return self._context

    def get_sys_prompt(self, _sys_PROMPT):
        self._sys_PROMPT = _sys_PROMPT
        self._context[0] = {'role': 'system', 'content': _sys_PROMPT} 

    def add_assistant(self, response_text):
        self._context.append({'role': 'assistant', 'content': response_text})
        return self._context

    def build_context(self, prompt: str):
        self._context.append({'role': 'user', 'content': prompt})

    def get_latest(self):
        return self._context[-1]

    def extend(self, context: list[ResponseOutputItem]):
        return self._context.extend(context)
from LLM.llm import llm

class IntelligenceLayer:
    def __init__(self):
        pass
    def process(self,context:list):
        try:
            response=llm(context)
            return response
        except Exception as e:
            raise Exception(f"Error in IntelligenceLayer: {e}")

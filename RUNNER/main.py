from OCHESTRATOR.Agent import Agent


if __name__ == "__main__":
    a = Agent()
    print("AI: Hello i am your personal ai assistant,enter quit or exit to stop")
    
    while True:
        user_prompt = input("USER: ")
        if user_prompt in ['quit','exit']:
            print("GoodBye!")
            break
        SYS_PROMPT = """You are a helpful personal AI assistant.

        When a task requires multiple tool calls (e.g. add, then divide, then power), you MUST:
        1. Call only ONE tool at a time.
        2. Wait for the result before calling the next tool.
        3. Use the returned value as input to the next tool call.
        4. Never nest tool calls or compose them in a single call.

        Example for "add 10 and 12, then divide by 2":
        - Step 1: call add(x=10, y=12) → wait for result (22)
        - Step 2: call div(x=22, y=2)  → wait for result (11)
        - Step 3: respond with the final answer

        Always follow this step-by-step pattern for chained operations.
        """
        a.set_sys_prompt(SYS_PROMPT)
        print("AI: "+a.step(user_prompt))

from langchain_mcp_adapters.client import MultiServerMCPClient  
from langchain.agents import create_agent
import asyncio
import os

# if using gemini models, create API key at https://aistudio.google.com/api-keys
os.environ["GOOGLE_API_KEY"] = input("Enter your Google API key:")


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",  # Local subprocess communication
                "command": "python",
                "args": ["math_server.py"],  # Change to your actual path
            },
        }
    )

    tools = await client.get_tools()
    # list all the available tools in the server
    print("Loaded tools:", tools)

    agent = create_agent(
        "google_genai:gemini-2.5-flash-lite",
        tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's square of 100"}]},
    )
    # prints the entire response in raw
    print("Math Response:", math_response)
    print("----------------------")

    # prints only the tool message, iow - the actual answer expected
    for msg in math_response['messages']:
        # If message is actually a ToolMessage object (not a dict), check its class name
        if type(msg).__name__ == "ToolMessage":
            print(msg.content)
        # If message is a dictionary or you want a fallback
        elif isinstance(msg, dict) and msg.get('tool_call_id'):
            print(msg['content'])

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's the sum of 8 and 8"}]}
    )
    print("----------------------")

    for msg in math_response['messages']:
        # If message is actually a ToolMessage object (not a dict), check its class name
        if type(msg).__name__ == "ToolMessage":
            print(msg.content)
        # If message is a dictionary or you want a fallback
        elif isinstance(msg, dict) and msg.get('tool_call_id'):
            print(msg['content'])

if __name__ == "__main__":
    asyncio.run(main())


from langchain_mcp_adapters.client import MultiServerMCPClient  
from langchain.agents import create_agent
import asyncio
import os
os.environ["GOOGLE_API_KEY"] = input("Enter Google API key:")


async def main():
    client = MultiServerMCPClient(
        {
            "weather": {
                "transport": "stdio",  # Local subprocess communication
                "command": "python",
                "args": ["weather_server.py"],  # Change to your actual path
            },
        }
    )

    tools = await client.get_tools()
    print("Loaded tools:", tools)

    agent = create_agent(
        "google_genai:gemini-2.5-flash-lite",
        tools
    )

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's the weather alerts in massachussets state"}]},
    )
    print("Weather Response:", weather_response)
    print("----------------------")

    for msg in weather_response['messages']:
        # If message is actually a ToolMessage object (not a dict), check its class name
        if type(msg).__name__ == "ToolMessage":
            print(msg.content)
        # If message is a dictionary or you want a fallback
        elif isinstance(msg, dict) and msg.get('tool_call_id'):
            print(msg['content'])

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather forecast at 31.9686° N, 99.9018° W (Texas)"}]},
    )
    #print("Weather Response:", weather_response)
    print("----------------------")

    for msg in weather_response['messages']:
        # If message is actually a ToolMessage object (not a dict), check its class name
        if type(msg).__name__ == "ToolMessage":
            print(msg.content)
        # If message is a dictionary or you want a fallback
        elif isinstance(msg, dict) and msg.get('tool_call_id'):
            print(msg['content'])
 
if __name__ == "__main__":
    asyncio.run(main())


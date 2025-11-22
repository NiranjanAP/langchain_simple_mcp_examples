from langchain_mcp_adapters.client import MultiServerMCPClient  
from langchain.agents import create_agent
import asyncio
import os
os.environ["GOOGLE_API_KEY"] = input("Enter Google API key:")


async def main():
    client = MultiServerMCPClient(
        {
            "exa": {
                "transport": "stdio",
                "command": "npx",
                "args": [
                    "-y",
                    "mcp-remote",
                    "https://mcp.exa.ai/mcp?tools=web_search_exa,get_code_context_exa"
                ]
            }
        }
    )

 
    tools = await client.get_tools()
    print("Loaded tools:", tools)

    agent = create_agent(
        "google_genai:gemini-2.5-flash-lite",
        tools
    )

    exa_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the latest news from NVIDIA"}]},
    )
    print("exa_response:", exa_response)
    print("----------------------")

    for msg in exa_response['messages']:
        # If message is actually a ToolMessage object (not a dict), check its class name
        if type(msg).__name__ == "ToolMessage":
            print(msg.content)
        # If message is a dictionary or you want a fallback
        elif isinstance(msg, dict) and msg.get('tool_call_id'):
            print(msg['content'])

 
if __name__ == "__main__":
    asyncio.run(main())


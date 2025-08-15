import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

nest_asyncio.apply()
async def main():
    # Connect to the server using SSE
    async with sse_client("http://127.0.0.1:8050") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            for tool in tools_result.tools:
                print(f" - {tool.name}: {tool.description}")

            # Call the calculator tool
            result = await session.call_tool("add", arguments={"a":2 ,"b":3})
            print(f"2 + 3 {result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(main())
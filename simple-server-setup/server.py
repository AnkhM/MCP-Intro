from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Create MCP Server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0", # Used for SSE transport (localhost)
    port = 6274 # Used for SSE transport
)

# Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

# Run the server
if __name__ == "__main__":
    transport = "stdio"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    else:
        ValueError(f"Unknown transport: {transport}")


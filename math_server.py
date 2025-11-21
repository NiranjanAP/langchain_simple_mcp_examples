from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("Simple Server")

# Define a simple tool/function exposed by this server
@mcp.tool()
def square(x: int) -> int:
    """Returns the square of a number."""
    return x * x

# Define a simple tool/function exposed by this server
@mcp.tool()
def add(x: int, y:int) -> int:
    """Returns the sum."""
    return x + y
    

if __name__ == "__main__":
    # Run MCP server with stdio transport (communicate over stdin/stdout)
    mcp.run(transport="stdio")

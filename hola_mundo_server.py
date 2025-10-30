from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Hello World Server")

@mcp.tool()
def say_hello(name: str) -> str:
    """Says hello to the given name"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Run the server in stdio mode
    mcp.run()

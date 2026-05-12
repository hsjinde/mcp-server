"""A minimal FastMCP demo server."""

from fastmcp import FastMCP

app = FastMCP("My MCP Server")


# 提供加法工具
@app.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
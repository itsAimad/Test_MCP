# #server.py
from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("AI Notes")

NOTES_FILE = 'notes.txt'

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE,'w') as f:
            f.write("")

@mcp.tool() # decorator: a design pattern in python that allows a user to add new functionality to an existing object without modifying its structure
def


#
# # Create an MCP server
# mcp = FastMCP("Demo")
#
# # Add an addition tool
#
# @mcp.tool()
# def add(a:int, b:int) -> int:
#     """ add two numbers """
#     return a + b
#
#
# @mcp.tool()
#
#
# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """Get a personalized greeting """
#     return f"Hello, {name}"
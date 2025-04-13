# #server.py
from mcp.server.fastmcp import FastMCP
import os


# Create an MCP server
mcp = FastMCP("AI Notes")

NOTES_FILE =  os.path.join(os.path.dirname(__file__),"notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE,'w') as f:
            f.write("")

@mcp.tool() # decorator: a design pattern in python that allows a user to add new functionality to an existing object without modifying its structure
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.

    Args:
        message(str): The note content to be added.
    Returns:
        str: Confirmation message indicating the note was saved.

    """
    ensure_file()
    with open(NOTES_FILE,'a') as f:
        f.write(message + '\n')
    return "Note saved!"

@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from sticky note file.

    Returns:
        str: All notes as a single string separated by line breaks.
            If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE,'r') as f:
        content = f.read().strip()
        return content or "No notes yet."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get latest line in notes
    Returns:
         str:the latest line in the notes

    """
    ensure_file()
    with open(NOTES_FILE,'r') as f:
        lines = f.readlines()
        return lines[-1].strip() if lines else "No notes yet."

@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI summarize all current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary
            If no notes exist, a message will be shown indicating that.

    """
    ensure_file()
    with open(NOTES_FILE,'r') as f:
        content = f.read().strip()
    if not content:
        return "There is no notes yet."
    return f"Summarize the current notes: {content} "



# DocString
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
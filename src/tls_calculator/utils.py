def count_tools(tool_string: str) -> int:
    if not isinstance(tool_string, str) or tool_string.strip() == "":
        return 0
    return len([t for t in tool_string.split(",") if t.strip()])

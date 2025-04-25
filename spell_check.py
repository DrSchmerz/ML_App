import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def analyze_spelling(text):
    matches = tool.check(text)
    return [{"message": m.message, "replacements": m.replacements} for m in matches]

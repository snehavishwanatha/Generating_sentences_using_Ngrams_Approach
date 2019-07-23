import grammar_check
tool = grammar_check.LanguageTool('en-US')
while True:
    text = raw_input("Enter  ")
    matches = tool.check(text)
    print matches
    print grammar_check.correct(text, matches)


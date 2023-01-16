def is_correct(seq):
    stack = []
    for char in seq:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return "NO"
            if char == ")" and stack[-1] != "(":
                return "NO"
            if char == "]" and stack[-1] != "[":
                return "NO"
            if char == "}" and stack[-1] != "{":
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"


sequence = input()
print(is_correct(sequence))

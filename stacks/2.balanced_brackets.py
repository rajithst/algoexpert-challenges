def balancedBrackets(string):
    stack = []
    for s in string:
        if s == "(" or s == "[" or s == "{":
            stack.append(s)
        elif s == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif s == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif s == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                return False
        else:
            continue
    return len(stack) == 0

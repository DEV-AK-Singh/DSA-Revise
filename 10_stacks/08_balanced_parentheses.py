def isValid(para_string): 
    stack = []
    for char in para_string:
        if char in ["(","[","{"]:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            bracket = stack.pop()
            if bracket == "(" and char != ")":
                return False
            elif bracket == "[" and char != "]":
                return False
            elif bracket == "{" and char != "}":
                return False 
    if len(stack) != 0:
        return False
    else:
        return True

print(isValid("(]"))
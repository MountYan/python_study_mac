# def isValid(s: str) -> bool:
#     # The stack to keep track of opening brackets.
#     stack = []

#     # Hash map for keeping track of mappings. This keeps the code very clean.
#     # Also makes adding more types of parenthesis easier
#     mapping = {")": "(", "}": "{", "]": "["}

#     # For every bracket in the expression.
#     for char in s:

#         # If the character is an closing bracket
#         if char in mapping:

#             # Pop the topmost element from the stack, if it is non empty
#             # Otherwise assign a dummy value of '#' to the top_element variable
#             top_element = stack.pop() if stack else '#'

#             # The mapping for the opening bracket in our hash and the top
#             # element of the stack don't match, return False
#             if mapping[char] != top_element:
#                 return False
#         else:
#             # We have an opening bracket, simply push it onto the stack.
#             stack.append(char)

#     # In the end, if the stack is empty, then we have a valid expression.
#     # The stack won't be empty for cases like ((()
#     return not stack


def isValid(s):
    a, b, c = "()", "[]", "{}"
    start, end = divmod(len(s), 2)
    if end:
        return False
    for _ in range(start):
        if a in s:
            s = s.replace(a, "")
        if b in s:
            s = s.replace(b, "")
        if c in s:
            s = s.replace(c, "")
    if s:
        return False
    return True


if __name__ == '__main__':
    s = "()"
    flag = isValid(s)
    print(flag)

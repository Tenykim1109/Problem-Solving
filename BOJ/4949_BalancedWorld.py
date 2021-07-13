import sys
input = sys.stdin.readline

while True:
    s = input()
    stack = []
    if s[0] == ".":
        break

    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if not stack or stack.pop() != "(":
                stack.append(c)
        elif c == "]":
            if not stack or stack.pop() != "[":
                stack.append(c)

    if stack:
        print("no")
    else:
        print("yes")
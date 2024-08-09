import sys

sys.stdin = open("sample_input(1).txt", "r")

T = int(input())
for tc in range(1, T+1):
    lst = list(map(str, input().split()))
    stack = []
    result = 0
    for i in lst:

        if i == ".":
            continue

        if i in "+*/-":
            if not stack:
                result = "error"
                break
            right = stack.pop()
            if not stack:
                result = "error"
                break
            left = stack.pop()
            if i == "+":
                result = left + right
            elif i == "-":
                result = left - right
            elif i == "*":
                result = left * right
            elif i == "/":
                result = int(left / right)

            stack.append(result)
        else:
            num = int(i)
            stack.append(num)
    if len(stack) > 1:
        result = "error"


    print(f"#{tc} {result}")
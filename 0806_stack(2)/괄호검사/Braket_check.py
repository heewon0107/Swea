import sys

sys.stdin = open("sample_input.txt", "r")

test = int(input())
for tc in range(1, test + 1):
    target = input()

    stack = []
    valid = True

    for tar in target:  # 타겟 순회
        if tar == "{" or tar == "(":
            stack.append(tar)

        elif tar == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                valid = False
                break

        elif tar == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                valid = False
                break
    if valid and not stack:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
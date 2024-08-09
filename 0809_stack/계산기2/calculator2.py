import sys
sys.stdin = open("input.txt", "r")

# 스택 밖에 있을 때 우선순위
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
# 스택 안에 있을 때 우선순위
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

def infix(string, n):                  # 중위 표기법을 상위표기법으로 바꾸는 함수
    stack = []
    postfix = ""
    for i in range(n):
        if string[i] in "+*":   # 연산자고
            if not stack:       # 스택이 없다면
                stack.append(string[i])
            else:               # 스택이 있고
                while stack and isp[stack[-1]] >= icp[string[i]]: # 우선순위가 크면
                    postfix += stack.pop()      # 스택에 쌓음
                stack.append(string[i])        # 스택에서 뽑음
        else:
            postfix += string[i]
    while stack:
        postfix += stack.pop()
    return postfix

def calculator(postfix):            # 상위 표기법 계산 함수
    stack = []
    result = 0
    for i in postfix:
        if i not in "+*":                # 피연산자가 나온다.
            stack.append(i)         # 스택에 추가한다.
        else:                       # 연산자가 나온다.
            if i == "+":
                result = int(stack.pop()) + int(stack.pop())    # 스택의 두개를 피연산자로 사용.
                stack.append(result)    # 결과를 스택에 넣어줌.
            elif i == "*":

                result = int(stack.pop()) * int(stack.pop())    # 스택의 두개를 피연산자로 사용.
                stack.append(result)    # 결과를 스택에 넣어줌.
    if stack:
        result = stack.pop()
    return result

T = 10
for tc in range(1, 1 + T):
    n = int(input())  # 줄 길이
    string = input()

    postfix = (infix(string, n))
    print(f"#{tc} {calculator(postfix)}")
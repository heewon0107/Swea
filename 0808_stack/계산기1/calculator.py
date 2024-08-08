import sys

sys.stdin = open("input.txt", "r")


def infix(string):                  # 중위 표기법을 상위표기법으로 바꾸는 함수
    stack = []
    postfix = ""
    for i in string:
        if i in "+" and not stack:  # 스택이 비어있고, 연산자가 나왔다.
            stack.append(i)         # 스택에 추가하자.
        elif i not in "+":          # 연산자가 아니고 피연산자다.
            postfix += i            # 후위 표기법에 추가하자.
            if stack:               # 근데 스택이 있으면
                postfix += stack.pop()  # 스택값을 추가해주자.
    return postfix                  # 함수의 결과는 후위표기법 완성본.

def calculator(postfix):            # 상위 표기법 계산 함수
    stack = []
    result = 0
    for i in postfix:
        if i != "+":                # 피연산자가 나온다.
            stack.append(i)         # 스택에 추가한다.
        else:                       # 연산자가 나온다.
            result = int(stack.pop()) + int(stack.pop())    # 스택의 두개를 피연산자로 사용.
            stack.append(result)    # 결과를 스택에 넣어줌.

    return result

T = 10
for tc in range(1, 1 + T):
    string_len = int(input())  # 줄 길이
    string = input()

    postfix = (infix(string))


    print(f"#{tc} {calculator(postfix)}")
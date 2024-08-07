import sys

sys.stdin = open("sample_input.txt", "r")

test = int(input())
for tc in range(1, test + 1):
    s = input()     # s = 문자열
    count = 0       # len 안 쓰고 길이 세기
    stack = []      # 스택 생성
    for i in s:
        if stack and stack[-1] == i:  #  스택의 마지막이 겹친다면.
            stack.pop()     # 겹친것을 지워준다.
        else:
            stack.append(i) # 겹친 것이 없으면 넣어주기.

    for _ in stack:         # 스택 길이 만큼 카운트 +1
        count += 1
    print(f"#{tc} {count}")
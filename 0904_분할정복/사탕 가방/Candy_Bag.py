import sys

sys.stdin = open("sample_input.txt", "r")

# 비율 생산하는 부분집합 만들기 ex [1,2,3,4]
def candy_rate(n):
    global result
    # 비율 맞추고 개수 맞췄다.

    if len(stack) == N and sum(stack) == M and stack[0] == min(stack):
        current_candy = divide_candy(stack)
        if current_candy > result:
            result = current_candy
        return

    if n == N:
        return
    for num in range(1, M - N + 1 + 1):
        stack.append(num)
        candy_rate(n + 1)
        stack.pop()


def divide_candy(rate):
    real_candy = max(candy)
    for i in range(N):
        # 지금의 최대 캔디 나누기 양
        if real_candy > candy[i] // rate[i]:
            real_candy = candy[i] // rate[i]
    return real_candy


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N종류의 사탕, M개 사탕이 있어야댐
    candy = list(map(int, input().split()))  # 캔디 종류의 개수
    candy.sort()
    stack = []  # 부분집합
    subset = [] # 부분집합 중복 확인
    result = 0

    candy_rate(0)
    print(f"#{tc} {result}")

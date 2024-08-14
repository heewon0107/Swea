import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split())) # 각 날의 매매가

    profit = 0
    current = 0
    while current < N:    # 매매가가를 다 돌때까지
        max_price = 0
        for i in range(current, N): # 최대 매매가 찾기
            if price[i] > max_price:
                max_price = price[i]
        # 최대값까지 팔기
        for i in range(current, N):
            if price[i] != max_price:
                profit += max_price - price[i]
            else:
                current = i + 1
                break

    print(f"#{tc} {profit}")
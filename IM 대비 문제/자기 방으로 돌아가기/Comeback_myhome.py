import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0] * 201
    for _ in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start

        start = (start + 1) // 2
        end = (end + 1) // 2
        for i in range(start, end+1):
            corridor[i] += 1
    t = max(corridor)
    print(f"#{tc} {t}")
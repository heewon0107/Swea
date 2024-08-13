import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    # 최대 idx = N - M + 1
    for i in range(N):
        for j in range(N):
            kill = 0
            for k in range(M):
                for l in range(M):
                    if i+k < N and j+l < N:
                        kill += arr[i+k][j+l]
            if kill > max_kill:
                max_kill = kill
    print(f"#{tc} {max_kill}")
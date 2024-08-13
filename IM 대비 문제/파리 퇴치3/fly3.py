import sys

sys.stdin = open("in1.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N):
        for j in range(N):
            kill = arr[i][j]
            for k in range(1, M):
                if 0 <= i - k:
                    kill += arr[i - k][j]
                if 0 <= j - k:
                    kill += arr[i][j - k]
                if i + k < N:
                    kill += arr[i + k][j]
                if j + k < N:
                    kill += arr[i][j + k]

    for i in range(N):
        for j in range(N):
            kill = arr[i][j]
            for k in range(1, M):
                if 0 <= i - k and i - k == j - k:
                    kill += arr[i - k][j - k]
                if i + k < N and i + k == j + k:
                    kill += arr[i + k][j + k]

            if kill > max_kill:
                max_kill = kill
    print(f"#{tc} {max_kill}")

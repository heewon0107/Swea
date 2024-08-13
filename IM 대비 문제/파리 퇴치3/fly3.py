import sys

sys.stdin = open("in1.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N):
        for j in range(N):
            kill1 = arr[i][j]
            for k in range(1, M):
                if 0 <= i - k:
                    kill1 += arr[i - k][j]
                if 0 <= j - k:
                    kill1 += arr[i][j - k]
                if i + k < N:
                    kill1 += arr[i + k][j]
                if j + k < N:
                    kill1 += arr[i][j + k]
            if kill1 > max_kill:
                max_kill = kill1
    for i in range(N):
        for j in range(N):
            kill2 = arr[i][j]
            for k in range(1, M):
                if 0 <= i - k and 0 <= j - k:
                    kill2 += arr[i - k][j - k]
                if 0 <= i - k and j + k < N:
                    kill2 += arr[i - k][j + k]
                if i + k < N and 0 <= j - k:
                    kill2 += arr[i + k][j - k]
                if i + k < N and j + k < N:
                    kill2 += arr[i + k][j + k]

            if kill2 > max_kill:
                max_kill = kill2
    print(f"#{tc} {max_kill}")

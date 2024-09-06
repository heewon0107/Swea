import sys

sys.stdin = open("input.txt", "r")

Delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chk = [0] * (N * N + 1)
    result = 0
    for i in range(N):
        for j in range(N):
            for di, dj in Delta:
                ni = i + di
                nj = j + dj

                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == arr[i][j] + 1:
                        chk[arr[i][j]] = 1
                        break

    cnt = max_cnt = start = 0
    for i in range(N * N + 1):
        if chk[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0

    print(f"#{tc} {start} {max_cnt + 1}")

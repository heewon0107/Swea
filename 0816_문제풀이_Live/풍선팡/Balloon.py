import sys

sys.stdin = open("input1.txt", "r")

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            now_v = balloon[i][j]
            for k in range(1, now_v + 1):
                for d in range(4):
                    nr = i + dr[d]*k
                    nc = j + dc[d]*k
                    if 0 <= nr < N and 0 <= nc < M:
                        now_v += balloon[nr][nc]
            if now_v > max_v:
                max_v = now_v
    print(f"#{tc} {max_v}")

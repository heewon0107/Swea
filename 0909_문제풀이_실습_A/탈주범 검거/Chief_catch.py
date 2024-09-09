import sys

sys.stdin = open("sample_input.txt", "r")

delta = [(), ([1, 0], [-1, 0], [0, 1], [0, -1]), ([1, 0], [-1, 0]), ([0, 1], [0, -1]), ([-1, 0], [0, 1]),
         ([1, 0], [0, 1]), ([0, -1], [1, 0]), ([-1, 0], [0, -1])]


def ternal(r, c, n):
    global result
    if n == L:
        return

    direction = arr[r][c]
    for di, dj in delta[direction]:
        nr = r + di
        nc = c + dj
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
            if direction == 1:
                if di == -1:
                    if arr[nr][nc] == 3 or arr[nr][nc] == 4 or arr[nr][nc] == 7:
                        continue
                elif di == 1:
                    if arr[nr][nc] == 3 or arr[nr][nc] == 5 or arr[nr][nc] == 6:
                        continue
                elif dj == -1:
                    if arr[nr][nc] == 2 or arr[nr][nc] == 6 or arr[nr][nc] == 7:
                        continue
                elif dj == 1:
                    if arr[nr][nc] == 2 or arr[nr][nc] == 4 or arr[nr][nc] == 5:
                        continue
            elif direction == 2:
                if di == 1:
                    if arr[nr][nc] == 3 or arr[nr][nc] == 5 or arr[nr][nc] == 6:
                        continue
                else:
                    if arr[nr][nc] == 3 or arr[nr][nc] == 4 or arr[nr][nc] == 7:
                        continue
            elif direction == 3:
                if dj == -1:
                    if arr[nr][nc] == 2 or arr[nr][nc] == 7 or arr[nr][nc] == 6:
                        continue
                else:
                    if arr[nr][nc] == 4 or arr[nr][nc] == 5 or arr[nr][nc] == 2:
                        continue
            elif direction == 4:
                if di == -1:
                    if arr[nr][nc] == 7 or arr[nr][nc] == 3 or arr[nr][nc] == 4:
                        continue
                else:
                    if arr[nr][nc] == 5 or arr[nr][nc] == 2 or arr[nr][nc] == 4:
                        continue
            elif direction == 5:
                if di == 1:
                    if arr[nr][nc] == 3 or arr[nr][nc] == 5 or arr[nr][nc] == 6:
                        continue
                else:
                    if arr[nr][nc] == 2 or arr[nr][nc] == 4 or arr[nr][nc] == 5:
                        continue
            elif direction == 6:
                if dj == -1:
                    if arr[nr][nc] == 2 or arr[nr][nc] == 6 or arr[nr][nc] == 7:
                        continue
                else:
                    if arr[nr][nc] == 6 or arr[nr][nc] == 5 or arr[nr][nc] == 3:
                        continue
            elif direction == 7:
                if dj == -1:
                    if arr[nr][nc] == 2 or arr[nr][nc] == 6 or arr[nr][nc] == 7:
                        continue
                else:
                    if arr[nr][nc] == 3 or arr[nr][nc] == 4 or arr[nr][nc] == 7:
                        continue
            visited[nr][nc] = 1
            escape[nr][nc] = 1
            ternal(nr, nc, n + 1)
            visited[nr][nc] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    escape = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    escape[R][C] = 1
    ternal(R, C, 1)
    for i in range(N):
        for j in range(M):
            if escape[i][j] == 1:
                result += 1
    print(f"#{tc} {result}")

import sys

sys.stdin = open("sample_input.txt", "r")


def mountain(i, j, cnt, visited):
    global result
    if i < 0 or i == N or j < 0 or j == N or visited[i][j]:
        return
    visited[i][j] = 1
    for di, dj in Delta:
        for k in range(K + 1):
            ni = i + di
            nj = j + dj
            if arr[i][j] > arr[ni][nj] - k:
                arr[ni][nj] -= k
                mountain(ni, nj, cnt + 1, visited)
                arr[ni][nj] -= k
            else:
                if cnt > result:
                    result = cnt
    visited[i][j] = 0


Delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            mountain(i, j, 0, [[0] * N for _ in range(N)])
    print(result)
import sys

sys.stdin = open("sample_input.txt", "r")


def mountain(i, j, cnt, visited, cut, h):
    global result
    if cnt > result:
        result = cnt

    for di, dj in Delta:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
            if arr[ni][nj] < h:
                visited.append((ni, nj))
                mountain(ni, nj, cnt + 1, visited, cut, arr[ni][nj])
                visited.pop()
            elif cut:
                for k in range(arr[ni][nj] - K, arr[ni][nj]):
                    if k < h:
                        visited.append((ni, nj))
                        mountain(ni, nj, cnt + 1, visited, 0, k)
                        visited.pop()


Delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    start = []
    high_top = 0
    for i in range(N):
        for j in range(N):
            if high_top < arr[i][j]:
                high_top = arr[i][j]
                start = [(i, j)]
            elif high_top == arr[i][j]:
                start.append((i, j))

    for r, c in start:
        mountain(r, c, 1, [(r, c)], 1, high_top)
    print(f"#{tc} {result}")

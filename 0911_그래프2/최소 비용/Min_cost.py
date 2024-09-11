from heapq import heappush, heappop

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra():
    q = [(0, 0, 0)]
    distance[0][0] = 0

    while q:
        r, c, w = heappop(q)

        if distance[r][c] < w:
            continue

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                h = 0
                if arr[nr][nc] > arr[r][c]:
                    h = arr[nr][nc] - arr[r][c]

                cost = distance[r][c] + 1 + h
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heappush(q, (nr, nc, cost))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    distance = [[1e9] * n for _ in range(n)]

    # 다익스트라 알고리듬
    dijkstra()

    print(f"#{tc} {distance[n - 1][n - 1]}")

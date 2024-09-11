import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def is_vaild(r,c):
    return 0 <= r < n and 0 <= c < n


dr = [1, -1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, 1, -1, -1, 1, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    bomb = [input() for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    bomb_num = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if bomb[i][j] == "*":
                for d in range(8):
                    ni = i + dr[d]
                    nj = j + dc[d]
                    if is_vaild(ni,nj) and bomb[ni][nj] != "*":
                        bomb_num[ni][nj] += 1

    # while True:
    #     while q:
    #         r, c = q.popleft()
    #         bomb_cnt = 0
    #         visited[r][c] = 1
    #         for d in range(8):
    #             nr = r + dr[d]
    #             nc = c + dc[d]
    #             if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
    #                 # 지뢰 없다.
    #                 if bomb[nr][nc] != "*":
    #                     # 다음 탐색을 위해 append 해주고 방문 체크
    #                     # bomb[nr][nc] = "*"
    #                     q.append((nr, nc))
    #                     visited[nr][nc] = 1
    #                 # 지뢰 있다. 다음 탐색을 위해선 카운트 하나 해야됨.
    #                 else:
    #                     bomb_cnt += 1
    #                     visited[nr][nc] = 1
    #         if bomb_cnt > 0:
    #             while q:
    #                 q.pop()
    #     if not start_search():
    #         break
    print(f"#{tc} {bomb_num}")

import sys

sys.stdin = open("input.txt", "r")

N = 16
# 델타 설정
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 시작 지점 찾기
def s_point(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


# 범위 인증
def is_vaild(r, c):
    return 0 <= r < N and 0 <= c < N


# 미로 찾기
def bfs(sr, sc, maze):
    # 방문 체크
    checked = [[0] * N for _ in range(N)]
    checked[sr][sc] = 1
    # 큐 생성
    q = []
    q.append((sr, sc))

    # 미로 탐방 시작
    while q:
        r, c = q.pop(0)
        if maze[r][c] == 3:
            return 1
        for i in range(N):
            for j in range(N):
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if is_vaild(nr, nc) and not checked[nr][nc] and maze[nr][nc] != 1:
                        checked[nr][nc] = 1
                        q.append((nr, nc))
    return 0


for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    sr, sc = s_point(maze)

    print(f"#{tc} {bfs(sr, sc, maze)}")
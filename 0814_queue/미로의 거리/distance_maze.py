import sys
sys.stdin = open("sample_input(1).txt", "r")

def is_vaild(r,c):
    return 0 <= r < N and 0 <= c < N

def search(r, c, root):
    # 방문기록
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1   # 시작 지점 체크
    # 큐 생성
    q = []
    q.append((r, c))
    # 델타 생성
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_vaild(nr, nc) and not visited[nr][nc]:
                if root[nr][nc] == 3:
                    return visited[r][c] - 1
                elif root[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1     # 방문 체크
                    q.append((nr, nc))  
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]
    sr = 0
    sc = 0
    # 시작 좌표 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j

    print(f"#{tc} {search(sr, sc, maze)}")
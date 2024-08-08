import sys

sys.stdin = open("sample_input(2).txt", "r")
T = int(input())


def maze_escape(i, j, N):
    visited[i][j] = 1
    if maze[i][j] == 3:
        return 1
    else:
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                if maze_escape(ni, nj, N):
                    return 1
        return 0


for tc in range(1, 1 + T):
    N = int(input())  # 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]  # 미로 생성

    visited = [[0] * N for _ in range(N)]
    # 0 = 통로, 1 = 벽, 2 = 출발점, 3 도착점

    # 출발점을 알고 위로 dfs를 사용하여 3에 도착시 break
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
                break

    print(f"#{tc} {maze_escape(start[0], start[1], N)}")

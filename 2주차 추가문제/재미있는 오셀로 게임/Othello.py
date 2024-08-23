def play(i, j, bw):
    board[i][j] = bw
    for di, dj in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        temp = []
        ni = i + di
        nj = j + dj
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:  # 반대 숫자다
            temp.append([ni, nj])
            ni += di
            nj += dj
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for x, y in temp:
                board[x][y] = bw


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 보드 크기, M = 돌을 놓는 횟수
    play_list = [list(map(int, input().split())) for _ in range(M)]  # 돌 놓는 위치

    board = [[0] * N for _ in range(N)]
    W = 2
    B = 1
    op = [0, 2, 1]
    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B
    board[N // 2][N // 2] = W

    for row, col, bw in play_list:
        play(row - 1, col - 1, bw)

    wcnt = bcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == W:
                wcnt += 1
            elif board[i][j] == B:
                bcnt += 1

    print(f"#{tc} {bcnt} {wcnt}")

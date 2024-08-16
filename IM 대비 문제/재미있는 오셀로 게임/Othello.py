import sys

sys.stdin = open("sample_input(1).txt", "r")


def othello(i, j, bw, N):
    board[i][j] = bw  # 자리에 돌 놓기
    for di, dj in [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [-1, -1], [-1, 1]]:
        ni = i + di
        nj = j + dj
        temp = []  # 뒤집을 돌을 저장할 리스트
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:
            temp.append((ni, nj))
            ni, nj = ni + di, nj +dj
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for p, q in temp:
                board[p][q] = bw



B = 1
W = 2
op = [0, 2, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 보드의 크기, M 돌을 놓는 횟수
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]  # 보드판

    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B
    board[N // 2][N // 2] = W

    for row, cul, bw in play:  # 돌놓기, 뒤집기
        othello(row - 1, cul - 1, bw, N)

    wcount = bcount = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcount += 1
            elif board[i][j] == W:
                wcount += 1
    print(f"#{tc} {bcount} {wcount}")
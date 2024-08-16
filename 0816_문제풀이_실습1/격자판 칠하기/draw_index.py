import sys

sys.stdin = open("sample_input.txt", "r")


def cheking(n, m):
    for r in range(n):
        for c in range(m):
            for d in range(2):  # 우 하 탐색
                ni = r + di[d]
                nj = c + dj[d]
                if ni < N and nj < M:  # 범위 설정
                    if board[r][c] == "#":  # "#이 나옴
                        if board[ni][nj] == "?":  # ? 나오면 변경
                            board[ni][nj] = "."
                        elif board[ni][nj] == "#":  # 체크무늬 실패
                            return "impossible"

                    elif board[r][c] == ".":  # "."이 나옴
                        if board[ni][nj] == "?":  # ? 나오면 변경
                            board[ni][nj] = "#"
                        elif board[ni][nj] == ".":  # 체크 무늬 실패
                            return "impossible"

    return "possible"


# 우측, 아래 탐색 델타
di = [0, 1]
dj = [1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxM 크기의 격자판
    board = [list(map(str, input())) for _ in range(N)]
    result = cheking(N,M)

    print(f"#{tc} {result}")
    # # = 검은색, . = 흰색 , ? = 아무거나
    # 격자판을 체크무늬로 할 수 있는지 판단하는 프로그램

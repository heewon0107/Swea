import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 1 + T):
    arr = [list(map(int, input().split())) for _ in range(9)]  # 9x9 퍼즐
    result = 1
    check_val = 45
    # 가로 세로 확인
    for i in range(9):
        count_i = [0] * 10
        count_j = [0] * 10
        for j in range(9):
            if count_i[arr[i][j]] != 1 and count_j[arr[j][i]] != 1:
                count_i[arr[i][j]] = 1
                count_j[arr[j][i]] = 1
            else:
                result = 0
    # 블럭 확인
    di = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    for i in [1, 4, 7]:
        for j in [1, 4, 7]:
            block_count = [0] * 10
            for d in range(9):
                ni = i + di[d]
                nj = j + dj[d]
                if block_count[arr[ni][nj]] != 1:
                    block_count[arr[ni][nj]] = 1
                else:
                    result = 0

    print(f"#{tc} {result}")

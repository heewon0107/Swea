import sys

sys.stdin = open("input.txt", "r")

test = 10
for tc in range(1, test + 1):
    m = int(input())  # 목표 회문 길이
    n = 8  # 8x8 배열
    count = 0
    string_arr = [list(map(str, input())) for _ in range(n)]  # 기존 배열
    rotate_arr = [[0] * n for _ in range(n)]  # 회전한 배열, Because , 회문을 쉽게 탐색
    for i in range(n):
        for j in range(n - 1, -1, -1):
            rotate_arr[i][j] = string_arr[j][i]

    for i in range(n):  # n행까지 탐색
        for j in range(n - m + 1):
            if string_arr[i][j:m + j] == string_arr[i][-n + m - 1 + j:-n + j - 1:-1]:  # 가로열에 회문 있는가?
                count += 1

            if rotate_arr[i][j:m + j] == rotate_arr[i][m + j - 1:-n + j - 1:-1]:  # 세로열에 회문 있는가?
                count += 1

    print(f"#{tc} {count}")

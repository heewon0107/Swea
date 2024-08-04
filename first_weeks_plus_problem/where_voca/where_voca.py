import sys

sys.stdin = open("input.txt", "r")

test_case = int(input())

for tc in range(1, test_case + 1):
    n, k = map(int, input().split())
    puzzle_arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    column_count = 0
    row_count = 0
    for i in range(n):
        for j in range(n):
            if puzzle_arr[i][j] == 1:   # 가로 탐색
                row_count += 1
            if puzzle_arr[i][j] == 0 or j == n - 1:
                if row_count == k:
                    result += 1
                row_count = 0

            if puzzle_arr[j][i] == 1:   #세로 탐색
                column_count += 1
            if puzzle_arr[j][i] == 0 or j == n - 1:
                if column_count == k:
                    result += 1
                column_count = 0

    print(f"#{tc} {result}")

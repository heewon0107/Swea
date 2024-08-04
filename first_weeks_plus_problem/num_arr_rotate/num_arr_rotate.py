import sys
sys.stdin = open("input.txt", "r")

test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())  # nXn 행렬

    num_arr = [list(map(int, input().split())) for _ in range(n)]
    degree_90 = [[0] * n for _ in range(n)]
    degree_180 = [[0] * n for _ in range(n)]
    degree_270 = [[0] * n for _ in range(n)]
    # 90도 회전
    for i in range(n):
        for j in range(n):
            degree_90[i][j] = num_arr[n - 1 - j][i]
    # 180도 회전
    for i in range(n):
        for j in range(n):
            degree_180[i][j] = degree_90[n - 1 - j][i]
    # 270도 회전
    for i in range(n):
        for j in range(n):
            degree_270[i][j] = degree_180[n - 1 - j][i]

    print(f"#{tc}")
    for i in range(n):  # 회전한 순서대로 윗줄부터 출력
        result_90 = "".join(map(str, degree_90[i]))
        result_180 = "".join(map(str, degree_180[i]))
        result_270 = "".join(map(str, degree_270[i]))
        print(result_90, result_180, result_270)

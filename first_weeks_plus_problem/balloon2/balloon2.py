import sys
sys.stdin = open("input1.txt", "r")

test_case = int(input())
for tc in range(1, test_case+1):
    n, m = map(int, input().split())
    balloon_arr = [list(map(int, input().split())) for _ in range(n)]

    max_value = 0
    # 우 상 좌 하
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    for i in range(n):
        for j in range(m):
            sum_flower = balloon_arr[i][j]
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < n and 0 <= nj < m:
                    sum_flower += balloon_arr[ni][nj]

            if max_value < sum_flower:
                max_value = sum_flower
    print(f"#{tc} {max_value}")
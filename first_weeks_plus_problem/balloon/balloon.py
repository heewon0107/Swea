import sys

sys.stdin = open("input1.txt", "r")

test_case = int(input())
for tc in range(1, test_case + 1):
    n, m = map(int, input().split())  # nXm
    arr_nxm = [list(map(int, input().split())) for _ in range(n)]
    #    상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, - 1, 1]
    max_value = 0
    ni, nj = 0, 0  # 현재 위치

    for i in range(n):
        for j in range(m):
            sum_value = arr_nxm[i][j]  # 처음 위치 값을 할당
            for k in range(1, arr_nxm[i][j] + 1):  # 처음 위치 값을 꽃가루 개수를 범위 지정
                for d in range(4):  # 개수만큼 터지는 풍선 위치값 ni,nj 생성
                    ni = i + di[d] * k  # 방향에 터지는 범위를 곱해줌
                    nj = j + dj[d] * k

                    if 0 <= ni < n and 0 <= nj < m:
                        sum_value += arr_nxm[ni][nj]
            if sum_value > max_value:
                max_value = sum_value
    print(f"#{tc} {max_value}")

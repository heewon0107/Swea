import sys

sys.stdin = open("input1.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxM 사진의 해상도
    place = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0
    for i in range(N):
        current_r = 0
        for j in range(M):
            if place[i][j] == 1:  # 가로 확인
                current_r += 1
            else:
                max_len = max(max_len, current_r)
                current_r = 0
        max_len = max(max_len, current_r)

    for j in range(M):
        current_c = 0
        for i in range(N):
            if place[i][j] == 1:  # 세로 확인
                current_c += 1
            else:
                max_len = max(max_len, current_c)
                current_c = 0
        max_len = max(max_len, current_c)

    print(f"#{tc} {max_len}")

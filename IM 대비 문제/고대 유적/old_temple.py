import sys

sys.stdin = open("input1.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxM 사진의 해상도
    place = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0

    for i in range(N):
        current_r = 0
        current_c = 0
        for j in range(M):
            if place[i][j] == 1:    # 가로 확인
                current_r += 1
                if current_r > max_len:
                    max_len = current_r
            else:
                current_r = 0

            if place[j][i] == 1:    # 세로 확인
                current_c += 1
                if current_c > max_len:
                    max_len = current_c
            else:
                current_c = 0
    print(f"#{tc} {max_len}")
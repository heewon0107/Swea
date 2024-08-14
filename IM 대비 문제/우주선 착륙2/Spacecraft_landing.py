import sys

sys.stdin = open("input2.txt", "r")

T = int(input())
# 델타 설정
dr = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxM 배열
    landing_place = [list(map(int, input().split())) for _ in range(N)]
    result_place = 0    # 예비 후보지 개수
    for i in range(N):
        for j in range(M):
            count = 0
            for d in range(9):
                nr = i + dr[d]
                nc = j + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    if landing_place[i][j] > landing_place[nr][nc]:
                        count += 1
            if count > 3:   # 현재 후보지가 사진 조망권
                result_place += 1
    print(f"#{tc} {result_place}")
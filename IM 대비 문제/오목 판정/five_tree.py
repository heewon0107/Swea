import sys

sys.stdin = open("sample_input.txt", "r")


def search(N, place):
    for i in range(N):
        stone_count_j = 0
        for j in range(N):
            if place[i][j] == "o":  # 행 탐색하다가 돌 발견
                stone_count_i = 1  # 카운트 추가
                stone_count_j += 1  # 카운트 추가
                stone_count_q = 1  # 카운트 추가
                stone_count_p = 1  # 카운트 추가

                if stone_count_j == 5:
                    return "YES"

                for k in range(1, N):  # 해당 N 까지 더해주며 탐색 시작
                    if i + k < N and place[i + k][j] == "o":  # 세로 탐색
                        stone_count_i += 1
                        if stone_count_i == 5:
                            return "YES"
                    else:
                        stone_count_i = 0
                    # 돌이 좌상단에 있을 때
                    if i + k < N and j + k < N and place[i + k][j + k] == "o":
                        stone_count_q += 1
                        if stone_count_q == 5:
                            return "YES"
                    else:
                        stone_count_q = 0
                    # 돌이 우상단에 있을 때
                    if i + k < N and 0 <= j - k and place[i + k][j - k] == "o":
                        stone_count_p += 1
                        if stone_count_p == 5:
                            return "YES"
                    else:
                        stone_count_p = 0
            else:
                stone_count_j = 0
    return "NO"


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # NxN 크기의 판
    place = [list(map(str, input())) for _ in range(N)]

    result = search(N, place)
    print(f"#{tc} {result}")
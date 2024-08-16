import sys

sys.stdin = open("sample_input.txt", "r")


def search_(magnet, direct_):

    if magnet + 1 < 4 and blade[magnet][2] != blade[magnet + 1][-2] and not checked[magnet + 1]:  # 오른쪽 탐색
        checked[magnet] = 1
        search_(magnet + 1, direct_ * -1)
    if 0 <= magnet - 1 and blade[magnet - 1][2] != blade[magnet][-2] and not checked[magnet - 1]:  # 왼쪽 탐색
        checked[magnet] = 1
        search_(magnet - 1, direct_ * -1)

    rotate_(magnet, direct_)


def rotate_(mag_num, dir_):
    if dir_ == clock:
        x = blade[mag_num].pop()
        blade[mag_num].insert(0, x)  # 날 회전
    else:  # 반시계
        y = blade[mag_num].pop(0)
        blade[mag_num].append(y)


T = int(input())
for tc in range(1, T + 1):
    K = int(input())  # K = 자석을 회전시키는 횟수
    blade = [list(map(int, input().split())) for _ in range(4)]  # 자석 4개의 날 정보
    rotate_mag = [list(map(int, input().split())) for _ in range(K)]  # K 번 회전하는 자석 정보

    # 방문 체크

    # 시계 방향 회전시 마지막 인덱스가 젤 앞으로옴.
    # 반시계 방향 회전시 0 인덱스를 팝해주고 어펜드
    # N극 = 0, S극 = 1
    # 시계방향 = 1, 반시계방향 = -1
    clock = 1
    counter_clock = -1
    n = 1
    s = 0
    for rotate in rotate_mag:
        first_mag = rotate[0]  # 회전시키는 자석
        direction_ = rotate[1]  # 회전방향
        checked = [0] * 5
        search_(first_mag - 1, direction_)  # 인덱스에는 -1 해줌
        # 회전 조건 앞 자석[2] 와 뒷 자석[-2] 이 달라야함.
    point_count = 1
    result = 0
    for i in blade:
        if i[0]:  # s면 true
            result += point_count
        point_count *= 2

    print(f"#{tc} {result}")

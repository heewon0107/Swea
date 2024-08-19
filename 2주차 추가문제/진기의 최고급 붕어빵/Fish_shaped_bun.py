import sys

sys.stdin = open("input.txt", "r")


def fish_shape_bun(n, m, k):
    bun = 0  # 붕어빵 개수
    t = 0
    count = 0
    while t <= 11111:
        t += 1
        if t % m == 0:  # m초 마다 k개 붕어빵 생성
            bun += k
        for time in arrive_time:
            if t == time:
                if bun == 0:
                    return "Impossible"
                else:
                    bun -= 1
                    count += 1
                    if count == n:
                        return "Possible"
    return "Possible"

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N = 사람 수, M = 시간초, K = 붕어빵 개수
    arrive_time = list(map(int, input().split()))  # N명의 사람이 도착하는 시간

    print(f"#{tc} {fish_shape_bun(N, M, K)}")

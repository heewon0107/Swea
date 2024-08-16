import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())


def runway(land, leng):
    count = 0
    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                for k in range(leng):
                    while 0 <= ni < N and 0 <= nj < 0 and land[i][j] == land[ni][nj]:   # 값이 변할 때까지 간다.
                        ni += di[d]
                        nj += dj[d]
                    # 새로운 값을 만남
                    if land[i][j] - 1 == land[ni][nj]:  # 높이 차이가 1이다.
                        for _ in range(1, k):
                            if 0 <= ni < N and 0 <= nj < 0


#   우측, 아래 탐색
di = [0, 1]
dj = [1, 0]

for tc in range(1, T + 1):
    N, X = map(int, input().split())  # N = 크기, X = 경사로의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 델타 확인 높거나 낮을 때까지 쭈욱 간다
    # 높으면 전에 경사로 길이만큼 +1해준뒤 경사로 전 값들이 -1이면 count +1
    # 낮으면 경사로 길이만큼 + 해준뒤 후 값이 -1 이면 +1

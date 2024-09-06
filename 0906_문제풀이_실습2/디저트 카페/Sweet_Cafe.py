import sys

sys.stdin = open("sample_input.txt", "r")


# 1. key 값이 같으면 안됌
# 2. 대각선 방향을 돌고 출발한 카페로 와야함
# 3. 한 번 초과하여 카페를 돌아야함
# 4. 왔던길을 돌아오면 안됌
delta = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
def naym(idx, jdx, cnt, start):
    global result
    global jj
    if start == 1 and start_point[0] == idx and start_point[1] == jdx:
        if cnt > result and cnt > 3:
            result = cnt
        return
    else:
        start = 1

    for di, dj in delta:
        ni = idx + di
        nj = jdx + dj

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and cafe[ni][nj] not in ate_sweet:
            visited[ni][nj] = 1
            ate_sweet.append(cafe[ni][nj])
            naym(ni, nj, cnt + 1, start)
            ate_sweet.pop()
            visited[ni][nj] = 0
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    ate_sweet = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0:
                if j == 0 or j == N:
                    continue
            if j == 0:
                if i == 0 or i == N:
                    continue
            start_point = [i, j]
            naym(i, j, 0, 0)
    if result < 4:
        result = -1
    print(f"#{tc} {result}")

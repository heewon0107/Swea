import sys

sys.stdin = open("sample_input.txt", "r")

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def isvaild(r, c):
    return 0 <= r < N and 0 <= c < N


def process(idx, l, connected, arr):
    global max_core_cnt, min_line_length

    if len(connected) + len(start) - idx < max_core_cnt:
        return

    if idx == len(start):
        if max_core_cnt < len(connected):
            max_core_cnt = len(connected)
            min_line_length = l
        elif max_core_cnt == len(connected):
            min_line_length = min(l, min_line_length)
        return

    r, c = start[idx]
    if (r, c) in connected:
        process(idx + 1, l, connected, arr)
    else:
        for d in range(4):
            nr, nc = r, c
            temp_list = []
            can_connect = True

            while True:
                nr += dr[d]
                nc += dc[d]
                if not isvaild(nr, nc):
                    break
                if arr[nr][nc] != 0:
                    can_connect = False
                    break
                temp_list.append((nr, nc))
            if can_connect:
                for vr, vc in temp_list:
                    arr[vr][vc] = 2
                process(idx + 1, l + len(temp_list), connected + [(r, c)], arr)
                for vr, vc in temp_list:
                    arr[vr][vc] = 0
        process(idx + 1, l, connected, arr)


results = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_core_cnt = 0
    result = 0
    min_line_length = N * N
    start = []
    connected_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    connected_list.append((i, j))
                start.append((i, j))
    process(0, 0, connected_list, arr)
    results. append(f"#{tc} {min_line_length}")

print(*results, sep="\n")

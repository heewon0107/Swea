import sys

sys.stdin = open("sample_input.txt", "r")


def breaking(level, remains, now_arr):
    global min_blocks
    if level == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return

    for col in range(W):
        copy_arr = [row[:] for row in now_arr]
        row = -1
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break
        if row == -1:
            continue

        li = [(row, col, copy_arr[row][col])]
        now_remains = remains - 1
        copy_arr[row][col] = 0

        while li:
            r, c, p = li.pop()
            for k in range(1, p):
                for i in range(4):
                    nr = r + (di[i] * k)
                    nc = c + (dj[i] * k)

                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue

                    if copy_arr[nr][nc] == 0:
                        continue

                    li.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    now_remains -= 1

        for c in range(W):
            idx = H - 1
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        breaking(level + 1, now_remains, copy_arr)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9
    blocks = 0

    for row in brick:
        for el in row:
            if el:
                blocks += 1

    breaking(0, blocks, brick)

    print(f"#{tc} {min_blocks}")

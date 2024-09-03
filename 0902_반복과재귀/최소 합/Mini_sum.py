import sys
sys.stdin = open("sample_input.txt", "r")

def maze(idx,jdx,total):
    global min_val
    if idx == N or jdx == N or total > min_val:
        return
    if idx == jdx == N - 1:
        total += arr[idx][jdx]
        if min_val > total:
            min_val = total
        return

    total += arr[idx][jdx]
    maze(idx + 1, jdx, total)
    maze(idx, jdx + 1, total)
    total -= arr[idx][jdx]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_val = 1000000
    maze(0,0,0)
    print(f"#{tc} {min_val}")


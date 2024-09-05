import sys
sys.stdin = open("input.txt", "r")

def work(idx, total):
    global result
    if total < result:
        return

    if idx == N:
        if result < total:
            result = total
        return

    for j in range(N):
        if done[j] == 1:
            continue
        if arr[idx][j] == 0:
            continue
        total *= arr[idx][j]/100
        done[j] = 1
        work(idx + 1, total)
        total /= arr[idx][j]/100
        done[j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    done = [0] * N
    work(0, 1)
    print(f"#{t} {result * 100:.6f}")
import sys

sys.stdin = open("sample_input(1).txt", "r")


def factory(idx, total):
    global result
    if total > result:
        return

    if idx == N:
        if result > total:
            result = total
        return

    for j in range(N):
        if done[j] == 1:
            continue
        total += arr[idx][j]
        done[j] = 1
        factory(idx + 1, total)
        total -= arr[idx][j]
        done[j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 99 * N
    done = [0] * N
    factory(0, 0)
    print(f"#{t} {result}")
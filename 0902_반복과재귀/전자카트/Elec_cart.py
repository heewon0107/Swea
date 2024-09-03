import sys

sys.stdin = open("sample_input.txt", "r")


def min_take(idx, i, total):
    global result
    # if total > result:
    #     return
    if idx == N:
        total += arr[i][0]
        if total < result:
            result = total
        return

    for j in range(N):
        # if i == j:
        #     continue

        if not checked[j]:
            total += arr[i][j]
            checked[j] = 1
            min_take(idx + 1, j, total)
            total -= arr[i][j]
            checked[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    checked = [0] * N
    checked[0] = 1
    result = 100 * N
    min_take(1, 0, 0)
    print(f"#{tc} {result}")

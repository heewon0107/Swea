import sys

sys.stdin = open("sample_input.txt", "r")


def cook(idx, A, B):
    global result
    if len(A) > N / 2 or len(B) > N / 2:
        return

    if idx == N:
        tA = tB = 0
        for i in range(N // 2):
            for j in range(N // 2):
                if i != j:
                    tA += arr[A[i]][A[j]]
                    tB += arr[B[i]][B[j]]
        result = min(result, abs(tA - tB))
        return

    cook(idx + 1, A + [idx], B)
    cook(idx + 1, A, B + [idx])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 20000 * 2
    cook(0, [], [])
    print(f"#{tc} {result}")

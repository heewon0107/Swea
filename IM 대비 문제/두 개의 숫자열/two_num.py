import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())        # N = A의 길이, M = B의 길이
    A = list(map(int, input().split()))     # A = 배열 1
    B = list(map(int, input().split()))     # B = 배열 2
    max_sum = 0

    if N > M:
        K = N-M
        for i in range(K+1):
            current = 0
            for j in range(M):
                if i+j < N and j < M:
                    current += A[i+j] * B[j]
            if current > max_sum:
                max_sum = current
    else:
        K = M - N
        for i in range(K+1):
            current = 0
            for j in range(N):
                if i + j < M and j < N:
                    current += A[j] * B[j+i]
            if current > max_sum:
                max_sum = current

    print(f"#{tc} {max_sum}")
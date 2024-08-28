import sys

sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, 1+1):
    N = int(input())    # 정점의 총 수

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(N):

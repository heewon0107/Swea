import sys
from collections import deque

sys.stdin = open("sample_input (1).txt", "r")


def cal(n, cnt):
    q = deque()
    q.append((n, cnt))
    visited[n] = 1

    while q:
        num, c = q.popleft()
        if num == M:
            return c

        for result in (num - 1, num + 1, num * 2, num - 10):
            if 0 <= result <= 1000000 and not visited[result]:
                visited[result] = 1
                q.append((result, c + 1))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    print(f"#{tc} {cal(N, 0)}")

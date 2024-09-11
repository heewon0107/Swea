import sys
from collections import deque

sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_list = [[] for _ in range(101)]
    visited = [0] * 101
    for i in range(0, n, 2):
        s = arr[i]
        e = arr[i + 1]
        adj_list[s].append(e)

    visited[start] = -1
    q = deque()
    q.append((adj_list[start], 1))

    while q:
        v, cnt = q.popleft()
        if type(v) == int:
            if not visited[v]:
                visited[v] = cnt
                q.append((v, cnt + 1))
        else:
            for next in v:
                if visited[next]:
                    continue
                visited[next] = cnt
                if adj_list[next]:
                    q.append((adj_list[next], cnt + 1))

    result = max(visited)
    for i in range(100, -1, -1):
        if visited[i] == result:
            print(f"#{tc} {i}")
            break

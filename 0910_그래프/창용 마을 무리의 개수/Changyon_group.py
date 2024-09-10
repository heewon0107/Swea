import sys
sys.stdin = open("s_input.txt", "r")

def group(node):
    visited[node] = 1
    if not adj_list[node]:
        return

    for i in adj_list[node]:
        if visited[i]: continue
        group(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]
    result = 0
    for _ in range(M):
        x, y = map(int, input().split())
        adj_list[x].append(y)
        adj_list[y].append(x)
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if visited[i]: continue
        group(i)
        result += 1
    print(f"#{tc} {result}")
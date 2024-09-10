import sys
sys.stdin = open("sample_input(1).txt", "r")

def group(i):
    global result
    visited[i] = 1
    if not adj_lst[i]:
        return

    for node in adj_lst[i]:
        if visited[node] == 1:
            continue
        group(node)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * (N+1)
    adj_lst = [[] for _ in range(N+1)]
    result = 0
    for i in range(0,M*2,2):
        adj_lst[arr[i]].append(arr[i+1])
        adj_lst[arr[i+1]].append(arr[i])

    for i in range(1,N+1):
        if visited[i]: continue
        group(i)
        result += 1
    print(f"#{tc} {result}")
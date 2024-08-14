import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")


def bfs(s, g, adj_l):
    # 방문기록
    visited = [0] * (V + 1)
    visited[s] = 1
    # 큐 생성
    q = deque()
    q.append(s)
    # 거리
    while q:
        t = q.popleft()
        for w in adj_l[t]:

            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
            if w == G:
                return visited[w] - 1

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V = 노드개수, E = 방향성이 없는 간선 개수
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj_l = [[] for _ in range(V + 1)]
    for i in range(E):
        V1, V2 = arr[i][0], arr[i][1]
        adj_l[V1].append(V2)
        adj_l[V2].append(V1)

    print(f"#{tc} {bfs(S, G, adj_l)}")

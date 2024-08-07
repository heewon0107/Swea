import sys

sys.stdin = open("sample_input.txt", "r")

# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프
# 특정한 두 개의 노드에 경로가 존재하는지 확인

# 경로가 있으면 1, 없으면 0 출력
# 노드번호는 1번부터 존재.
# V개의 노드 중에는 간선으로 연결되지 않은 경우 존재할 수도 있고 안 할 수도있고

def dfs_m(s, V):
    visited = [0] * V   # 방문체크
    stack = []          # 스택 설정
    visited[s-1] = 1      # 시작 노드는 방문 처리
    v = s - 1             # 현재 방문하고 있는 정점

    while True:
        for i in range(0, V):
            if start_end_node[v][i] and visited[v] == 0:    # 갈 노드가 존재하고, 방문한 적이 없다면.
                stack.append(v)     # 노드를 스택에 쌓아준다.
                print(stack)


            if start_end_node[v][i] == G:
                print(f"#{tc} 1")


test = int(input())
for tc in range(1, test+1):
    V, E = map(int, input().split())    # V = 노드 , E = 간선 수
    start_end_node = [list(map(int, input().split())) for _ in range(E)]  # start = 출발, end = 도착
    S, G = map(int, input().split())    # S = 출발 노드, G = 도착 노드


    stack = []      # 스택 생성

    v = S      # v = 현재 위치 , 처음엔 출발 노드로 할당.

    # v 노드에서 출발해서 end
    if start_end_node[v] and start_end_node[v] != G: #
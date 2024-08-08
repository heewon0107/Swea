import sys

sys.stdin = open("sample_input.txt", "r")

# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프
# 특정한 두 개의 노드에 경로가 존재하는지 확인

# 경로가 있으면 1, 없으면 0 출력
# 노드번호는 1번부터 존재.
# V개의 노드 중에는 간선으로 연결되지 않은 경우 존재할 수도 있고 안 할 수도있고

def dfs_m(s, V, G):
    visited = [0] * V     # 방문체크
    stack = []            # 스택 설정
    visited[s-1] = 1      # 시작 노드는 방문 처리
    v = s - 1             # 현재 방문하고 있는 정점
    print(v+1)            # 노드 번호 출력 (1부터 시작)

    while True:
        if v == G-1:      # 도착 노드를 거친 경로가 있다면
            global result
            result = 1
            break
        for i in adj_list[v]:
            if visited[i-1] == 0:    # 갈 노드가 존재하고, 방문한 적이 없다면.
                stack.append(v)          # 노드를 스택에 쌓아준다.
                print(i)

                visited[i-1] = 1
                v = i - 1
                break       # 새로 바뀐 v 에서 연결된 정점을 찾자.
        else:   # 여기가 실행되면 break는 만난 적이 없다.=> 갈 수 있는 노드를 못 찾음.
                # 되돌아 가야한다
            if stack:
                v = stack.pop()
            else:
                break

test = int(input())
for tc in range(1, test+1):
    V, E = map(int, input().split())    # V = 노드 , E = 간선 수
    start_end_node = [list(map(int, input().split())) for _ in range(E)]  # start = 출발, end = 도착
    S, G = map(int, input().split())    # S = 출발 노드, G = 도착 노드
    result = 0      # 출력할 결과
    adj_list = [[] for _ in range(V)]
    for start, end in start_end_node:   # 시작점과 종점을 인접 리스트에 인덱스와 값으로 할당.
        adj_list[start-1].append(end)
    dfs_m(S, V, G)  # 출발 노드와 노드 수 도착 노드를 인자로 활용
    print(f"#{tc} {result}")

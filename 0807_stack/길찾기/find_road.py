import sys
sys.stdin = open("input.txt", "r")

# 길찾기 dfs 사용
# A = 0 , B = 99 노드는 0부터 99까지 한 노드당 갈림길은 최대 2개다.

def dfs_m(s, adj_list):
    # 방문체크
    visited = [[0] * 100]  # 노드는 100개다.

    # 스택설정
    stack = []

    # 시작 정점은 방문 처리
    visited[s] = 1

    # 현재 방문하고 있는 정점
    v = s

    while True:
        for i in range(2):
            if adj_list[v][i] and visited[adj_list[v][i]] == 0: # 노드가 있고, 방문기록이 없다.
                v = adj_list[v][i]  # 그 방으로 정점 이동
                visited[v] = 1
                stack.append(v)
                print(stack)        # 스택을 쌓아준다.
                if v == 99:
                    print(f"#{shop} 1")
                    break
            else:   # 방이 비어있으면
                v = stack.pop() # 스택 줄어들고 전 방으로 간다.
        else:   # break가 된적이 없으면.
            print(f"#{shop} 0")
            break


test_case = 1
for tc in range(1, test_case +1):
    shop, V = map(int,input().split())      # s = 날리기, 간선쌍 개수
    arr = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]     # 노드는 0~99
    for i in range(0, V*2, 2):              # 16 개의 간선 쌍으로 간선은 X2
        v1, v2 = arr[i], arr[i+1]   # 시작 노드와 도착 노드 할당.
        adj_list[v1].append(v2)     # 각 노드의 도착 노드들을(최대 2개) 할당


dfs_m(0, adj_list)   # 시작 노드, 간선 쌍 개수, 인접 리스트
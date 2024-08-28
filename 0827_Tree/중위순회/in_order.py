import sys

sys.stdin = open("input.txt", "r")

def in_order(node):
    global result
    if node > N or not node:
        return

    # 중위 순위 시작
    in_order(left[node])
    result += node_key[node]
    in_order(right[node])

T = 10
for tc in range(1, T+1):
    N = int(input())    # 정점의 총 수
    result = ""
    left = [0] * (N + 1)    # 각 인덱스별 왼자식
    right = [0] * (N + 1)   # 각 인덱스별 우자식
    node_key = [0] * (N + 1)    # 노드의 key
    for i in range(N):
        arr = input().split()
        node_key[i+1] = arr[1]
        if len(arr) >= 3:
            left[i+1] = int(arr[2])
        if len(arr) == 4:
            right[i+1] = int(arr[3])
    in_order(1)
    print(f"#{tc} {result}")
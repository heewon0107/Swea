import sys

sys.stdin = open("sample_input.txt", "r")


def bst(node):
    # 범위 이탈
    if left[node] == 0:
        return node_key[node]

    # 리프 노드 값 더해줌.
    # node_key[node] = node_key[node] + bst(left[node])
    # node_key[node] = bst(right[node]) + bst(right[node])
    # 현재 노드의 값을 리턴해줌
    node_key[node] += bst(left[node]) + bst(right[node])
    return node_key[node]

T = int(input())
for tc in range(1, T + 1):
    # N = 노드의 개수, M = 리프 노드의 개수, L = 값을 출력할 노드
    N, M, L = map(int, input().split())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    node_key = [0] * (N + 1)  # 해당 노드의 값.
    # 리프 노드에 값 삽입
    for leaf, value in [map(int, input().split()) for _ in range(M)]:
        node_key[leaf] = value

    for i in range(2, N + 1):
        if i % 2 == 0:
            left[i // 2] = i
        else:
            right[i // 2] = i
    bst(1)

    print(f"#{tc} {node_key[L]}")

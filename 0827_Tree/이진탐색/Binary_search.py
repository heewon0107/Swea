import sys

sys.stdin = open("sample_input(1).txt", "r")


def dfs(node):
    global root
    global result1, result2
    # 자식이 없음
    if node == 0:
        return

    dfs(left[node])
    if node == 1:  # 1번 노드(루트에 도달)
        result1 = root
    if node == N // 2:
        result2 = root
    root += 1
    dfs(right[node])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 노드의 수
    root = 1  # 루트 넘버
    result1 = 0
    result2 = 0
    left = [0] * (N + 1)  # 왼쪽 자식
    right = [0] * (N + 1)  # 오른쪽 자식

    for i in range(2, N + 1):
        if i % 2 == 0:  # 짝수
            left[i // 2] = i
        else:  # 홀수
            right[i // 2] = i

    dfs(root)
    print(f"#{tc} {result1} {result2}")

import sys

sys.stdin = open("sample_input.txt", "r")

# 탐색할 루트 찾기
def tree(root):
    # leaf가 없다.
    if not left[root]:
        return
    # 탐색할 루트 찾음
    if root == N:
        subset(root)
        return
    tree(left[root])
    tree(right[root])

# 서브트리 탐색하기.
def subset(x):
    global result
    if left[x] == 0:
        return
    result += 1
    subset(left[x])
    subset(right[x])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E = 간선의 개수, N = 루트
    arr = list(map(int, input().split()))
    adj_lst = [[] for _ in range(E + 2)]  # 인접리스트 번호
    left = [0] * (E + 3)
    right = [0] * (E + 3)
    result = 0
    for i in range(0, E * 2, 2):
        adj_lst[arr[i]].append(arr[i + 1])

    for i in range(1, E + 2):
        if adj_lst[i]:  # 간선이 있을 경우
            left[i] = adj_lst[i][0]
            if len(adj_lst[i]) == 2:
                right[i] = adj_lst[i][1]

    tree(arr[0])
    print(f"#{tc} {result}")

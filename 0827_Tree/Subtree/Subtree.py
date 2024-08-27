import sys

sys.stdin = open("sample_input.txt", "r")


# 탐색할 루트 찾기
def tree(root):
    global result
    global certification    # 서브트리 자격 부여

    # leaf가 없다.
    if not root:
        return

    # 서브 트리면 카운팅
    if certification == 1:
        result += 1
    # 서브트리 탐색할 루트 찾음
    if root == N:
        certification = 1   # 서브트리 카운트 자격 부여.
        tree(left[root])
        tree(right[root])
        certification = 0   # 서브트리 종료 하면서 본인 노드 결과에 추가
        result += 1
    else:
        tree(left[root])
        tree(right[root])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E = 간선의 개수, N = 루트
    arr = list(map(int, input().split()))
    adj_lst = [[] for _ in range(E + 2)]  # 인접리스트 번호
    # 노드 번호는 E+1번까지 0번 인덱스는 안 씀
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    result = 0
    certification = 0
    for i in range(0, E * 2, 2):
        adj_lst[arr[i]].append(arr[i + 1])

    for i in range(1, E + 2):
        if adj_lst[i]:  # 간선이 있을 경우
            left[i] = adj_lst[i][0]
            if len(adj_lst[i]) == 2:
                right[i] = adj_lst[i][1]

    tree(arr[0])
    print(f"#{tc} {result}")

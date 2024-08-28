import sys
import math

sys.stdin = open("sample_input.txt", "r")


def tree(lev):
    # 1개 짜리 tree면 return
    if level == 1:
        return True
    # 각 레벨에서 대칭 확인하기 위함.
    for i in range(1, lev):
        # 대칭확인 수는 level 만큼 해줌.
        for j in range(i):
            if node_key[(2 ** i) + j] != node_key[(2 ** i) * 2 - 1 - j]:
                return False

    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N = 트리의 크기
    arr = list(map(int, input().split()))
    node_key = [0] * (N + 1)
    # level은 아래 공식. N + 1 = 2**level
    level = int(math.log2(N + 1))

    # 각 노드의 키 값 삽입
    for i in range(N):
        node_key[i + 1] = arr[i]

    print(f"#{tc} {tree(level)}")

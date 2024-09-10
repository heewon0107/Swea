import sys

sys.stdin = open("input.txt", "r")


def dfs(node, cnt):
    global max_cnt, result

    visited[node] = 1
    # 갈 데가 없다.
    if not adj_lst[node]:
        # 여기가 마지막인가?
        if cnt > max_cnt:
            max_cnt = cnt
            result = node
        elif cnt == max_cnt:
            # 마지막이고 결과 값이 큰거 출력
            if result < node:
                result = node
        return

    # 다음 연락망이 있다.
    for i in adj_lst[node]:
        if visited[i]: continue
        dfs(i, cnt + 1)


for tc in range(1, 11):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_lst = [[] for _ in range(101)]
    for i in range(0, n, 2):
        adj_lst[arr[i]].append(arr[i + 1])
    max_cnt = 0
    result = 0
    visited = [0] * 101

    dfs(start, 0)
    print(f"#{tc} {result}")

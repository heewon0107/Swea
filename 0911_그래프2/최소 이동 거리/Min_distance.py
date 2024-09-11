import sys

sys.stdin = open("sample_input(2).txt", "r")


def min_distance(node, point):
    global result
    # 마지막 번호닷
    if node == n:
        if result > point:
            result = point
        return
    if point > result:
        return

    # 갈 곳이 있다.
    if adj_lst[node]:
        for next, add_ in adj_lst[node]:
            min_distance(next, point + add_)

T = int(input())
for tc in range(1, T + 1):
    n, E = map(int, input().split())  # n = 마지막 연결 지점, e = 도로의 개수
    arr = [list(map(int, input().split())) for _ in range(E)]
    adj_lst = [[] for _ in range(E)]
    result = 1e9
    for s, e, w in arr:
        adj_lst[s].append((e, w))

    min_distance(0, 0)
    print(f"#{tc} {result}")

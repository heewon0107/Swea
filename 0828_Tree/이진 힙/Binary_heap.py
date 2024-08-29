def enq(n):
    global last
    last += 1   # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모>자식 비교를 위해
    p = c//2    # 부모번호 계산
    while p >= 1 and h[p] > h[c]:   # 부모가 있는데, 더 크면
        h[p], h[c] = h[c], h[p]  # 교환
        c = p
        p = c//2


T = int(input())
for tc in range(1, T+1):
    N = int(input())          # 필요한 노드 수
    arr = list(map(int, input().split()))

    h = [0]*(N+1)   # 최대힙
    last = 0        # 힙의 마지막 노드 번호
    result = 0
    for num in arr:
        enq(num)

    while last > 1:
        result += h[last//2]
        last //= 2
    print(f"#{tc} {result}")
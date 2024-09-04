def sqr(s, e):
    global result
    if s > e:
        return
    mid = s - (s - e) // 2
    if mid ** 2 == x:
        result = mid
        return
    elif mid ** 2 > x:
        sqr(s, mid - 1)
    else:
        sqr(mid + 1, e)



T = int(input())
for tc in range(1, T + 1):
    x = int(input())
    result = 0
    sqr(0, x)
    print(f"#{tc} {result}")
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        width = 0
        for j in range(M):
            if arr[i][j]:
                width += 1
                if result < width:
                    result = width
            else:
                width = 0

    for i in range(M):
        height = 0
        for j in range(N):
            if arr[j][i] == 1:
                height += 1
                if result < height:
                    result = height
            else:
                height = 0
    if result < 2:
        result = 0
    print(f"#{tc} {result}")
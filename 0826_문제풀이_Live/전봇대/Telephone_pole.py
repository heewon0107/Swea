T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 전선의 개수
    line = [list(map(int, input().split())) for _ in range(N)]
    line.sort()

    cnt = 0     # 교차점 수
    for i in range(1, N):   
        for j in range(i):  # A는 더 낮지만 B가 더 높은 경우 교차
            if line[j][1] > line[i][1]:
                cnt += 1

    print(f"#{tc} {cnt}")
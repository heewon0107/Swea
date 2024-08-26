n = 1
s = 2

T = 10
for tc in range(1, T+1):
    N = int(input())    # 한 변의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0     # 교착 상태 개수
    for i in range(N):
        np = 0
        for j in range(N):
            if arr[j][i] == n:  # n극을 만남.
                np = n
            elif np == n and arr[j][i] == s:  # n극이 s극을 만남
                cnt += 1
                np = 0
    print(f"#{tc} {cnt}")
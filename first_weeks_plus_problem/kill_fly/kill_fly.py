import sys
sys.stdin = open("input.txt", "r")

test_case = int(input())
for tc in range(1, test_case+1):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]

    # 최대한 많은 파리를 죽여야 한다.
    # fly[0,0] 부터 fly[n-1,n-1] 까지 많은 파리를 찾아보자.
    kill_max = 0
    for i in range(n-m+1):  # 파리채 행 범위

        for j in range(n-m+1):  #파리채 열 범위
            kill_fly = 0
            for k in range(m):  # 파리채 범위 안의 파리 수
                for l in range(m):
                    kill_fly += fly[i+k][j+l]
            if kill_fly > kill_max:
                kill_max = kill_fly
    print(f"#{tc} {kill_max}")
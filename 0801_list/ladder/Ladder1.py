import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint as print
from copy import deepcopy
# 양 옆에 or 사용 1이 있으면 방향 변경
# 바닥에 도착 하면 멈춤 <[][]

# 달팽이 델타 생성 좌, 우, 아래 만 알면 됨
# 0 1 2
# 아래 오른쪽 왼쪽
di = [1, 0, 0]
dj = [0, 1, -1]
d = [0, 1, 2]   # 방향


for tc in range(1, 11):
    icu = int(input())
    new_ladder = [list(map(int, input().split())) for _ in range(100)]
    solving = 0     # 2가 나오는 j열 사다리값
    ni, nj = 0, 0   # 사다리 시작 지점
    for j in range(100):         # X = 0 부터 99까지
        ni, nj = 0, j   # 사다리 시작 지점
        ladder = deepcopy(new_ladder)
        if ladder[0][j] == 1  :   # X 축의 시작이 1 이면 시작.
            while ni < 100:      # 수직 거리가 99가 될 때까지              
                if nj + 1 < 100 and ladder[ni][nj+1] == 1 :   # 우측에 1있음
                    nj = nj + dj[1]  
                    ladder[ni][nj-1] = 0  
                elif 0 <= nj - 1 and ladder[ni][nj-1] == 1:   # 좌측에 1있음
                    nj = nj + dj[2]
                    ladder[ni][nj+1] = 0
                else:
                    ni = ni + di[0]      # 수직 이동 거리
            if ladder[ni-1][nj] == 2 :
                solving = j
                break
    print(f"#{tc} {solving}")
    # print(new_ladder[0][57 : 68])



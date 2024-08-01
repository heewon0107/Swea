import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint as print

# 양 옆에 or 사용 1이 있으면 방향 변경
# 바닥에 도착 하면 멈춤 <[][]

# 달팽이 델타 생성 좌, 우, 아래 만 알면 됨
# 0 1 2
# 아래 오른쪽 왼쪽
di = [-1, 0, 0]
dj = [0, 1, -1]
d = 0   # 방향
r, c = 0, 0     # 처음 자리
test_case = int(input())
for tc in range(1, test_case+1):
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):    # X = 0 부터 99까지
        if j != 0 :         # X 축의 시작이 0 이면 시작을 안함.
            while ni < 100:  # 수직 거리가 99가 될 때까지
                for i in range(100):

                    ni = i + di[d]      # 수직 이동 거리
                    nj = j + dj[j]      # 수평 이동 거리
                if ladder[i][j] == 2 :

# 내려가는 경우의 수
# 1. 옆의 숫자보다 클 때
# 2. 옆의 숫자가 0일 때
# 3.


print(ladder)
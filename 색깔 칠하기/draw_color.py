import sys
sys.stdin = open("sample_input.txt", "r")
from pprint import pprint 

T = int(input()) + 1

for tc in range(1, T):
    n = int(input())    # 첫 줄에 칠할 영역의 개수
    maximum = 10
    temp = [[0] * 10 for i in range(maximum)]   # maximum X maximum 격자 생성
    purple = 0      # 겹친 보라색 수
    for i in range(n):  # 영역의 개수 만큼 받기
        left_i, left_j, right_i, right_j, color = map(int, input(). split()) 

        for i in range(left_i, right_i + 1):        # 입력받은 인덱스에 color 입력 인덱스 
            for j in range(left_j, right_j + 1):    # 
                
                if temp[i][j] == 0:      # target이 빈 공간이면 색깔 칠하기
                    temp[i][j] = color      # 입력받은 위치에 color (1 or 2) 할당
                elif temp[i][j] != color: # 다른 색이 칠해져있으면 보라색 +1
                    purple += 1

    print(f"#{tc} {purple}")
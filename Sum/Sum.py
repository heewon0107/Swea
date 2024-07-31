import sys
sys.stdin = open("input.txt", "r")

tc = 0
while tc < 10:
    tc = int(input())
    max_value = 0         # 최댓값
    num_list = [list(map(int, input().split())) for _ in range(100)]    # 입력받은 100개의 수를 리스트에 100번 담음

    # 행 최대값 구하기
    for i in range(100):
        million_num = 0     # 한 행 요소들의 합 [1,2,3... 100]
        for j in range(100):

            million_num += num_list[i][j]       # 인덱스 0~99 까지의 합 = 한 행의 합(가로)
        if max_value < million_num:         #  더한 값을 현재 최대값과 비교후 크면 할당
            max_value = million_num

    # 열 최대값 구하기 
    for j in range(100):
        million_num = 0     # 한 열의 요소들의 합 (세로)
        for i in range(100):
            million_num += num_list[i][j]       # 인덱스 0~99 까지의 합 = 한 열의 합(세로)
        if max_value < million_num:      
            max_value = million_num

    # 대각선 최대값 구하기 방향 >
    million_num = 0
    for i in range(100): 
        for j in range(100):
            if i == j:      # i = j 라면 대각선으로 진행 가능
                million_num += num_list[i][j]       # 대각선 더하기
    if max_value < million_num:      
        max_value = million_num

    # 대각선 최대값 구하기 방향 <
    million_num = 0            
    for i in range(100):    
        for j in range(99,-1,-1):
            if i + j == 99 :
                million_num += num_list[i][j] 

    if max_value < million_num:      
        max_value = million_num

    print(f"#{tc} {max_value}")
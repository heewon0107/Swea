for tc in range(1, 11): #평탄화 전
    dump_num = int(input())
    high_list = list(map(int, input(). split()))
     
    for i in range(dump_num): # 평탄화 작업
 
        max_value = high_list[0]
        min_value = high_list[0]
        max_idx = 0
        min_idx = 0
        for  i in range(100): # 맥스 미니값과 인덱스
            if high_list[i] > max_value:
                max_value, max_idx = high_list[i], i
                 
            if high_list[i] < min_value:
                min_value, min_idx = high_list[i], i
        high_list[max_idx] -= 1    
        high_list[min_idx] += 1  
 
        # 두번째 for 반복으로 max_value 값과 min_value 값 찾음
        # high_list[max_value의 인덱스] -= 1
    max_value = high_list[0]
    min_value = high_list[0]
    for i in range(1,100):
        if high_list[i] > max_value:
            max_value = high_list[i] 
             
        if high_list[i] < min_value:
            min_value = high_list[i]
 
    result = max_value - min_value
 
    print(f"#{tc} {result}") 
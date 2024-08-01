for tc in range(1, 11): 
    dump_num = int(input())
    high_list = list(map(int, input(). split()))

    for i in range(dump_num): # 평탄화 끝
        high_value = max(high_list)
        # 제일 큰친구 -1 제일 작은친루 +1
        low_value = min(high_list)
 
        high_list[high_list.index(high_value)] -= 1
        high_list[high_list.index(low_value)] += 1
 
    high_flat = max(high_list)
    low_flat = min(high_list)
    result = high_flat - low_flat
    print(f"#{tc} {result}") 
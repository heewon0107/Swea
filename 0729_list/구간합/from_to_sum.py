test_case = int(input())

for tc in range(1, test_case + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    
    
    min_sum = 100*10000
    max_sum = 0
    for k in range(n-m+1):
        total = 0
        for j in range(k, k+m) :
            total += numbers[j]

        if total > max_sum :
            max_sum = total
        if total < min_sum :
            min_sum = total
        

            
    
    print(f"#{tc} {max_sum - min_sum}")
test_case = int(input()) # 테스트 케이스 개수

for i in range(1, test_case + 1) :
    n = int(input()) # 정수 개수
    numbers = list(map(int, input().split())) # n개의 양수 

    for x in range(n-1, 0, -1): 
        for y in range(x):
            if numbers[y] > numbers[y+1] : 
                numbers[y], numbers[y+1] = numbers[y+1], numbers[y] # y, y+1 교환
    max_value = numbers[-1] # 마지막 자리 맥스값
    min_value = numbers[0] # 첫 자리 미니값

    difference_value = max_value - min_value  # 차이 = 맥스 - 미니
    print(f"#{i} {difference_value}")

import sys

sys.stdin = open("input.txt", "r")

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = input()
    max_count = 0 # 최대값
    current_count = 0 # 현재 값
    
    for i in arr:
        if i is "1":
            current_count += 1
            max_count = max(current_count, max_count)
        else:
            current_count = 0

    print(f"#{tc} {max_count}")    


    
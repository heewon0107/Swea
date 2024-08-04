import sys
sys.stdin = open("carrot_sample_in.txt", "r")

test_case = int(input())

for tc in range(1, test_case + 1):
    carrot = int(input())
    size_carrot_list = list(map(int,input().split()))

    max_sequence = 0    # 커지는 당근 개수 최대값
    current_sequence = 0    # 현재 커지는 당근 개수
    before_size = 0
    for size in size_carrot_list:
        
        if size > before_size:  # 커지면 +1
            current_sequence += 1
            if max_sequence < current_sequence: # 최대 연속 커지는 숫자를 할당
                max_sequence = current_sequence    
        else:
            current_sequence = 1    # 커지지 않으면 다시 1로 돌아옴
        before_size = size  # 비교할 크기를 재할당 해줌
    print(f"#{tc} {max_sequence}")

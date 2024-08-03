import sys

sys.stdin = open("GNS_test_input.txt", "r")

test_case = int(input())
for tc in range(1,test_case+1):  # , test_case + 1
    shop = input()
    num_list = list(input().split())
    num_transform = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    num_dict = {}
    for i in range(10):
        num_dict[num_transform[i]] = i  # {zeo : 0}
    counts = [0] * 10
    result = [0]*len(num_list) # num_list 길이 만큼의 변경 될 결과 리스트 생성
    for num in num_list:
        counts[num_dict[num]] += 1  # 넘리스트의 넘버의 카운트를 + 1

    # 누적 카운팅 만들기.
    for i in range(1, 10):
        counts[i] = counts[i] + counts[i-1]

    # 누적카운트를 범위로 숫자 할당
    for i in range(0, len(counts)):        # 700, 1416, 2135, 2869, 3548, 4285, 4959, 5613, 6337, 7041
        if result[0] == 0:  # ZRO 자리는 범위가 0 부터 인덱스[0] 까지이므로 깍두기
            for x in range(0, counts[i]):
                result[x] = num_transform[i]
        else:
            for x in range(counts[i-1], counts[i]):
                result[x] = num_transform[i]
    print(f"#{tc}")
    print(*result)

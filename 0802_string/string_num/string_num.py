import sys
sys.stdin = open("sample_input(1).txt", "r")

test_case = int(input())
for tc in range(1, test_case+1):
    str1 = input()
    str2 = input()
    counting_dict = {}
    for i in str1:
        counting_dict[i] = 0    # 초기 문자 할당.

    max_value = 0
    for itm in str2:    # str2 의 원소가 카운팅 대상이면 카운팅
        if itm in counting_dict:
            counting_dict[itm] += 1
            if counting_dict[itm] > max_value:
                max_value = counting_dict[itm]

    print(f"#{tc} {max_value}")

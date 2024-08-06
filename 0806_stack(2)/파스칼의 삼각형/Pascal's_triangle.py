import sys

sys.stdin = open("input.txt", "r")

# r = 0 # j열 이동
#
# if r < n:
#     print(*value_list)
#     # 인덱스 0과 1을 더한 건 다음 줄의 1,  1,2를 더하면 다음줄의 2
#     value = value_list[r] + value_list[r+i]
#     value_list.append(value)
#     r += 1

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())  # 파스칼의 삼각형의 크기

    print(f"#{tc}")
    value_list = []  # 초기값 설정.

    for i in range(n):     # 4 [2,3]

        if len(value_list) < 2:
            value_list.append(1)
            print(*value_list)

        # elif len(value_list) == 2:
        #     value = value_list[i - 1] + value_list[i - 2]
        #     value_list.insert(i - 1, value)
        #     print(*value_list)
        else:

            value = value_list[i-1] + value_list[i - 2]
            value_list.insert(i-1, value)
            print(*value_list)
            if len(value_list) != n:
                value = value_list[i - 1] + value_list[i - 2]
                value_list.insert(i - 1, value)
                print(*value_list)


        # length < 2 이면 append(1)
        # length >= 2 이면 첫 줄의 [n]+ [n-1] 이
        #                 두번째 줄의 n 값

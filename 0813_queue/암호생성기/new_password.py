import sys

sys.stdin = open("input.txt", "r")

TC = 10
for tc in range(1, TC + 1):
    test = input()
    password_list = list(map(int, input().split()))

    while password_list[-1] > 0:        # 마지막 자리에 0이 나오면 종료
        for i in range(1, 6):           # 1부터 5까지 빼주기 반복
            password_list[0] = password_list[0] - i     # 앞자리에서 빼주고 뒤로 넘겨주기
            if password_list[0] <= 0:   # 만약 빼줬는데 0 이하면
                password_list[0] = 0    # 0으로 고정
                password_list.append(password_list[0])  # 맨뒤로 넘기고
                password_list.pop(0)    # 앞자리 빼주기
                break                   # 그리고 결과 값 출력하기 위해 break
            else:
                password_list.append(password_list[0])  # 빼줬는데 1 이상이면 계속 반복
                password_list.pop(0)

    print(f"#{tc}", *password_list)
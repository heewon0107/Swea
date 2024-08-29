import sys

sys.stdin = open("input (1).txt", "r")

pwd = {"0001101": 0,
       "0011001": 1,
       "0010011": 2,
       "0111101": 3,
       "0100011": 4,
       "0110001": 5,
       "0101111": 6,
       "0111011": 7,
       "0110111": 8,
       "0001011": 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    code = 0
    # 코드 배열 찾기
    for i in range(N):
        if '1' in arr[i]:
            code = arr[i]
            break
    # 56개의 코드 값 추출
    for j in range(M - 1, 0, -1):
        if code[j] == '1':
            code = code[j - 55: j+1]
            break
    # 10진수로
    password = [0] * 8
    num = 0
    for i in range(0, 56, 7):
        password[num] = int(pwd[code[i:i + 7]])
        num += 1
    # 홀수 합
    odd = password[0] + password[2] + password[4] + password[6]
    # 짝수 합
    even = password[1] + password[3] + password[5] + password[7]

    left = odd * 3
    result = even + left
    if result % 10 == 0:
        result = sum(password)
    else:
        result = 0
    print(f"#{tc} {result}")
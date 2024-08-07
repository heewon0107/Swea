import sys

sys.stdin = open("input.txt", "r")

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())  # 파스칼의 삼각형의 크기

    print(f"#{tc}")
    value_list = []
    temp = 0
    for i in range(n):  # 4 [2,3]
        new_list = value_list.copy()
        for j in range(i + 1):
            if j == i or j == 0:  # 마지막 자리에 1
                value_list.append(1)

            else:
                value_list[j] = new_list[j-1] + new_list[j]

        print(*value_list[temp: temp+i+1])

# 정석
arr = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i -1][j]

        print(arr[i][j], end=" ")
    print()
import sys

sys.stdin = open("sample_input.txt", "r")

test_case = int(input())
for tc in range(1, test_case + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):

            if i % 2 == 0:
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
    list_print = []
    for i in range(10):
        list_print.insert(i, arr[i])    # 최대 배열 길이는 10
    print(f"#{tc}", *list_print)    # 언패킹 과정
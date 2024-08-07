import sys
sys.stdin = open("sample_input.txt", "r")

test_case = int(input())
for tc in range(1, test_case + 1):
    N = int(input()) // 10   # 가로 길이

    paste = [0] * (N+1) # 붙이는 리스트 생성
    paste[1] = 1
    paste[2] = 3
    for i in range(3, N+1):
        paste[i] = paste[i-1] + (2 * paste[i-2])
    print(f"#{tc} {paste[N]}")





import sys

sys.stdin = open("input.txt", "r")

test_case = int(input())

for tc in range(1, test_case + 1):
    n, k = map(int, input().split())
    puzzle_arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    # 행에 있는 단어 찾기
    for i in range(n):
        for j in range(n - k):  # 갈수있는 j의 범위
            total = 0
            for t in range(k):  # 움직일 수 있는 범위
                total += puzzle_arr[i][j + t]
            if total == k:
                result += 1
    print(f"#{tc} {result}")

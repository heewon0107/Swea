import sys
sys.stdin = open("sample_input(1) (1).txt", "r")

def search(n, idx, s, selected):
    global min_sum

    if s > min_sum: # 합이 최소값보다 크면 가지치기
        return

    if idx == n:    # 범위를 벗어났고
        if min_sum > s:
            min_sum = s
            return

    for i in range(n):
        if not selected[i]:
            selected[i] = 1     # i 열 선택 체크
            s += arr[idx][i]    # 합에 더해주고

            search(n, idx+1, s, selected)   # 다음 행 찾아가기

            selected[i] = 0 # 다음 i 도 봐야하니 다시 초기화
            s -= arr[idx][i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = N * 9  # 최대값 27
    i_check = 0

    search(N, 0, 0, [0]*N)

    print(f"#{tc} {min_sum}")
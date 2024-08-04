import sys

sys.stdin = open("sample_input.txt", "r")

test_case = int(input())
for tc in range(1, test_case + 1):
    n, m = map(int, input().split())
    lst = list(input() for _ in range(n))
    rotate = [[0] * n for _ in range(n)]
    for i in range(n):  # 회전한 배열 만들기
        for j in range(n):
            rotate[i][j] = lst[j][i]
        rotate[i] = ''.join(rotate[i])  # 회전했을 때 리스트값이기 때문에 문자열로 변경해준다.

    result = 0  # 회문 결과 변수
    for i in range(0, n - m + 1):   # n-m 만큼 범위를 변경해줘야 한다.
        for j in range(n):      # 행 열의 최대 값인 n만큼 탐색을 해야한다.
            if i - 1 == -1:  # 범위가 -1이 되버리면 마지막 자리가 되버리므로 공백으로 변경해준다.
                if m + i <= n and lst[j][i:m + i] == lst[j][m + 1::-1]:  # j행의 순서가 역순과 같으면
                    result = lst[j][i:m + i]
                elif m + i <= n and rotate[j][i:m + i] == rotate[j][m + 1::-1]:  # 열 중에 같은게 있으면.
                    result = rotate[j][i:m + i]
            elif m + i <= n:
                if lst[j][i:m + i] == lst[j][m + i: i - 1: -1]:     # 행 중에 있다.
                    result = lst[j][i: m + i]
                elif rotate[j][i:m + i] == rotate[j][m + i: i - 1: -1]:     # 열 중에 있다
                    result = rotate[j][i: m + i]
    print(f"#{tc} {result}")

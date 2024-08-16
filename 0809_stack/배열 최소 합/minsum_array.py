import sys
sys.stdin = open("sample_input(1) (1).txt", "r")

T = int(input())
# idx : idx 번째 행에서 하나씩 돌아야 함
def min_sum(idx, checked_i, checked_j, N):
    result = []     # 합의 최대 값
    if idx == N:
        return
    if checked_i[idx] == 1:    # idx 열에 숫자가 있으면
        return
    # if len(result) == 3:
    #     result.append(sum(lst))

    for j in range(N):
        if not checked_j[j]:   # check 를 안했으면
            lst.append(arr[idx][j])
            result += arr[idx][j]
            checked_j[j] = 1
            min_sum(idx + 1, checked_i, checked_j, N)


        print(lst)
        print(checked_j)
    # return min(result)
    # idx + 1 행으로 가서 가장 작은 숫자를 고른다. checked[idx][j] = 1
for tc in range(1, 2):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    checked_i = [0] * N
    checked_j = [0] * N
    lst = []
min_sum(0, checked_i, checked_j, N)
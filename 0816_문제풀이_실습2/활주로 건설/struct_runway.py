import sys

sys.stdin = open("sample_input.txt", "r")


def check_i(idx):  # 인덱스 범위 안에서 탐색한다.   0~N-1
    construct = [0] * N
    for k in range(1, N):
        # 왼쪽이 클 경우 = 오른쪽에 경사로를 놓아야함
        if arr[idx][k - 1] > arr[idx][k]:
            for stack in range(X):  # 경사로 배치할 구간 탐색
                if not k + stack < N:  # 인덱스 범위 벗어나면 리턴
                    return False
                if arr[idx][k - 1] - 1 != arr[idx][k + stack]:  # 경사로 길이 만큼 같아야 함.
                    return False
                if construct[k+stack]:  # 건설한 경사로가 있다면 건설 불가
                    return False
                construct[k + stack] = 1    # 경사로 건설
        # 오른쪽이 클 경우 = 왼쪽에 경사로를 놓아야 함.
        elif arr[idx][k - 1] < arr[idx][k]:
            for stack in range(X):
                if not 0 <= k - 1 - stack:
                    return False
                if arr[idx][k - 1 - stack] != arr[idx][k] - 1:
                    return False
                if construct[k - 1 - stack]:
                    return False
    return True


def check_j(jdx):  # 인덱스 범위 안에서 탐색한다.  위아래 탐색
    construct = [0] * N
    for k in range(1, N):
        # 위에가 더 클 경우 = 아래에 경사로를 놓아야함
        if arr[k - 1][jdx] > arr[k][jdx]:
            for stack in range(X):  # 경사로 배치할 구간 탐색
                if not k + stack < N:  # 인덱스 범위 벗어나면 리턴
                    return False
                if arr[k - 1][jdx] - 1 != arr[k + stack][jdx]:  # 경사로 길이 만큼 같아야 함.
                    return False
                if construct[k + stack]:
                    return False

                construct[k + stack] = 1
        # 아래가 더 클 경우 = 위에 경사로를 배치해야함
        elif arr[k][jdx] > arr[k - 1][jdx]:
            for stack in range(X):  # 경사로 배치할 구간 탐색
                if not 0 <= k - 1 - stack:  # 인덱스 범위 벗어나면 리턴
                    return False
                if arr[k][jdx] - 1 != arr[k - 1 - stack][jdx]:  # 경사로 길이 만큼 같아야 함.
                    return False
                if construct[k - 1 - stack]:
                    return False
                construct[k - 1 - stack] = 1
    return True

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())  # N = 크기, X = 경사로의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for x in range(N):
        if check_i(x):  # 가로방향 경사로 건설
            count += 1
        if check_j(x):  # 세로방향 경사로 건설
            count += 1

    print(f"#{tc} {count}")
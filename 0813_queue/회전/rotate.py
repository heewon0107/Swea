import sys
sys.stdin = open("sample_input.txt", "r")

Test = int(input())

for tc in range(1, Test + 1):
    N, M = map(int, input().split())    # N = 숫자의 개수, M = 작업 횟수
    num_list = list(map(int, input().split()))  # q에 넣을 숫자 리스트
    q = [0] * N
    front = rear = -1

    for i in range(M):  # 0~9까지 10번
        rear += 1
        if i < N:   # 처음 큐 범위까지는 쌓아줌
            q[rear % N] = num_list[rear % N]  # q 범위는 0~2
        else:       # 맨 앞에서 뒤로 옮긴다.
            back = q.pop(0)
            q.append(back)
    print(f"#{tc} {q[0]}")
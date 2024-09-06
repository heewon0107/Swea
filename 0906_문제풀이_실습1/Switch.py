import sys

sys.stdin = open("switch_sample_in.txt", "r")

for tc in range(1, int(input()) + 1):
    N = int(input())
    switch = list(map(int, input().split()))
    target = list(map(int, input().split()))
    cnt = 0
    button = [1, 0]
    for i in range(N):
        if switch[i] == target[i]:
            continue
        for j in range(i, N):
            switch[j] = button[switch[j]]

        cnt += 1
    print(f"#{tc} {cnt}")

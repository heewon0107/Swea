import sys
sys.stdin = open("input.txt", "r")

def top(idx, total):
    global result
    if total - B > result:
        return
    if idx == N:
        if 0 <= total - B < result:
            result = total - B
        return

    top(idx + 1, total + tall_lst[idx])
    top(idx + 1, total)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    tall_lst = list(map(int, input().split()))
    result = B
    top(0, 0)
    print(f"#{tc} {result}")
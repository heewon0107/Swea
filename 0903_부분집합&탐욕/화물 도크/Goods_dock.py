import sys

sys.stdin = open("sample_input(1).txt", "r")


def dock(arr, cnt, stack):
    global result
    if cnt > result:
        result = cnt

    for item in arr:
        if stack[-1][-1] <= item[0] and item != stack[-1]:
            stack.append(item)
            cnt += 1
            dock(arr, cnt, stack)
            stack.pop()
            cnt -= 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in arr:
        dock(arr, 1, [i])

    print(f"#{tc} {result}")

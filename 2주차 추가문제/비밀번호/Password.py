import sys

sys.stdin = open("input.txt", "r")


def pwd(n):
    for i in range(n):
        if i+1 < n and arr[i] and arr[i] == arr[i+1]:  # 앞뒤가 같으면.
            arr.pop(i+1)
            arr.pop(i)
            pwd(n-2)
            return

T = 10
for tc in range(1, T+1):
    N, M = map(str, input().split())
    X = int(N)
    arr = list(M)
    pwd(X)
    result = "".join(arr)
    print(f"#{tc} {result}")
import sys

sys.stdin = open("input.txt", "r")


def search(exchan):
    global result
    if exchan == N:
        result = max(result, int("".join(map(str, stack))))
        return
    for i in range(n - 1):
        for j in range(i + 1, n):
            stack[i], stack[j] = stack[j], stack[i]
            chk = int("".join(map(str, stack)))
            if (exchan, chk) not in v:
                search(exchan + 1)
                v.append((exchan, chk))
            stack[i], stack[j] = stack[j], stack[i]


T = int(input())
for tc in range(1, T + 1):
    A, N = map(int, input().split())
    lst = list(str(A))
    stack, v = [], []
    n = len(lst)
    result = 0
    for i in lst:
        stack.append(i)
    search(0)
    print(f"#{tc} {result}")

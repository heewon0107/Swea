T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    eat = 0
    while C <= B:
        B -= 1
        eat += 1
    while B <= A:
        A -= 1
        eat += 1
    if A < 1:
        eat = -1
    print(f"#{tc} {eat}")
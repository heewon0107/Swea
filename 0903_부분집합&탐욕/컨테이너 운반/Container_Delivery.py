import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 컨테이너 수, M = 트럭 수
    weight = list(map(int, input().split()))
    power = list(map(int, input().split()))
    result = 0

    while weight:
        W = max(weight)
        P = max(power)
        if W <= P:
            weight.pop(weight.index(W))
            power.pop(power.index(P))
            result += W
        else:
            weight.pop(weight.index(W))
        if not power:
            break

    print(f"#{tc} {result}")

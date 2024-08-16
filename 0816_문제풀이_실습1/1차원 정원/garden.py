import sys

sys.stdin = open("sample_input.txt", "r")

def water(n,d):
    X = n   # 남은 꽃의 개수
    w = 0   # 필요한 분무기 수
    while X > 0:   # 꽃에 물을 다 줄 때까지
        X -= 1 + 2 * d  # 분무기의 범위만큼 빼줌
        w += 1
    return w

T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())    # N = 꽃의 개수, D = 분무기의 성능
    result = water(N, D)
    print(f"#{tc} {result}")


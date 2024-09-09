T = int(input())
p = []
for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    result = min(B, D) - max(A, C)
    if result < 0:
        result = 0
    p.append(result)

for index, result in enumerate(p):
    print(f"#{index + 1} {result}")
T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    result = ""
    x = N
    while x != 0:
        x = x * 2
        if x >= 1:
            result += "1"
            x = x - 1
        else:
            result += "0"
    if len(result) > 12:
        result = "overflow"
    print(f"#{tc} {result}")

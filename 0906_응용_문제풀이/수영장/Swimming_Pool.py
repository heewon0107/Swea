import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    day, month, three_month, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = min(dp[i-1] + day * plan[i], dp[i-1] + month)

        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + three_month)

    result = min(dp[12], year)
    print(f"#{tc} {result}")
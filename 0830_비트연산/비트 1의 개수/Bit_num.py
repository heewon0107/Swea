import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bn = bin(N)
    result = 0
    for i in range(2,len(bn)):
        if bn[i] == "1":
            result += 1
    print(f"#{tc} {result}")
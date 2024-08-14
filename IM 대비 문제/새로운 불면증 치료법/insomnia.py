import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    count = [0] * 10
    o_o = 0
    while sum(count) < 10:
        o_o += 1
        xN = str(N * o_o)   # str으로 바꿔주고
        for i in xN:        # 다시 변경
            count[int(i)] = 1
    print(f"#{tc} {xN}")
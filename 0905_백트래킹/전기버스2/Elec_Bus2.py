import sys
sys.stdin = open("sample_input.txt", "r")

def go(position, cnt):
    global result
    # 종점 도착
    if result < cnt:
        return
    if position >= bus_stop[0]:
        result = cnt - 1
        return

    for i in range(1, bus_stop[position] + 1):
        go(position+i, cnt+1)

T = int(input())
for tc in range(1, T+1):
    bus_stop = list(map(int, input().split()))
    result = 100
    go(1, 0)
    print(f"#{tc} {result}")
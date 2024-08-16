import sys

sys.stdin = open("sample_input.txt", "r")

def eat(candy):
    eat = 0
    for i in range(2, 0, -1):
        while candy[i-1] >= candy[i]:
            candy[i-1] -= 1
            eat += 1
            if candy[i-1] < 1:
                return -1

    return eat

T = int(input())
for tc in range(1, T+1):
    candy = list(map(int, input().split())) # 캔디들
    result = eat(candy)


    print(f"#{tc} {result}")
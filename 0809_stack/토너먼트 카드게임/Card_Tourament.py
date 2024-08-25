import sys

sys.stdin = open("sample_input.txt" ,"r")

def winner(i, j):
    if i == j:
        return i

    l = winner(i, (i+j)//2)     # 좌측 플레이어
    r = winner((i+j)//2 + 1, j) # 우측 플레이어
    if (card_num[l] == 1 and card_num[r] == 2) or (card_num[l] == 2 and card_num[r] == 3) or (card_num[l] == 3 and card_num[r] == 1):
        return r
    else:
        return l
T = int(input())

for tc in range(1, T+1):
    N = int(input())    # N = 인원수
    card_num = list(map(int, input().split()))  # N 명이 고른 카드

    win_man = winner(0, N - 1) + 1

    print(f"#{tc} {win_man}")
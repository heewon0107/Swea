import sys

sys.stdin = open("sample_input(2).txt", "r")


def rb(arr, player):
    global result
    n = len(arr)
    if n < 3:
        return True
    arr.sort()
    for i in arr:
        if (i+1 in arr and i+2 in arr) or arr.count(i) == 3:
            result = player
            return False
    return True

T = int(input())
for tc in range(1, T + 1):
    card_lst = list(map(int, input().split()))
    result = 0
    card_1 = []
    card_2 = []
    card = 0
    while rb(card_1, 1) and rb(card_2, 2) and card < 12:
        card_1.append(card_lst[card])
        card += 1
        card_2.append(card_lst[card])
        card += 1

    print(f"#{tc} {result}")
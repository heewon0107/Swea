import sys
sys.stdin = open("input.txt", "r")
test_case = int(input())

for tc in range(1, test_case + 1):
    n = int(input())    # 카드 장 수
    card_num = input()   # 카드에 적힌 숫자
    card_list = []  # 카드 넘버를 리스트화

    for i in card_num:
        card_list.append(int(i))
    # print(f"카드 숫자 목록 : {card_list}")

    count = [0] * (max(card_list) + 1)  # 숫자 개수 세는 리스트
    # 개수 별로 카운트 리스트 안에 넣기

    for i in card_list:
        count[i] += 1
    # print(f"숫자 개수 목록 {count}")

    max_value = 0   # 리스트 중 최댓값
    max_count = 0   # 리스트 중 최빈값
    for i in card_list:

        if count[i] > max_count:    # 최빈 수를 최댓값, 최빈 값에 할당
            max_value = i
            max_count = count[i]
        elif count[i] == max_count: # 최빈 값이 겹칠 때,
            if i > max_value:   # 더 큰 수를 반환
                max_value = i


    print(f"#{tc} {max_value} {max_count}")
import sys
sys.stdin = open("input.txt", "r")
test_case = int(input())

for tc in range(1, test_case +1):
    n = input()
    score_list = list(map(int, input().split()))

    dict_score = {} # {"빈도수" : "최빈값"}

    for score in score_list:
        frequnet = score_list.count(score)  # 리스트의 점수마다 반복수를 딕셔너리에 저장
        dict_score[frequnet] = score    # 빈도수 : 점수
    max_fre = max(dict_score)   # 최빈값 

    print(f"#{tc} {dict_score[max_fre]}")
    
import sys
sys.stdin = open("sample_input.txt", "r")

test = int(input())
for tc in range(1,test+1):
    s = input() # s = 문자열

    tl = len(s) # s의 텍스트 길이

    ti = 0  # s의 텍스트 순회 인덱스
    pi = 0  # 패턴을 찾기 위한 전 문자

    while ti < tl: # 패턴을 찾으면 패턴 삭제 후 종료
        pi = s[ti]  # ti번째의 문자.

        if pi == pi[ti-1]:  # 문자열이 반복되면.
            # s[ti], s[ti-1] 를 삭제하고싶은데.

        ti += 1

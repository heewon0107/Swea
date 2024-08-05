import sys
sys.stdin =open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    pattern = input()   # 패턴
    text = input()      # 총 텍스트

    pl = len(pattern)   # 패턴길이
    tl = len(text)      # 텍스트 길이

    yam = 0   # 패턴 발견 수
    pi, ti = 0, 0       # 패턴과 텍스트 순회 인덱스

    while pi < pl and ti < tl:  #   인덱스 값 벗어나면 종료.
        if pattern[pi] != text[ti]:     # 다르면
            ti = ti - pi    # 순회한 길이만큼 빼주고
            pi = -1
        ti += 1     # 순회당 +1
        pi += 1     # 순회당 +1

        if pl == pi:    # 패턴길이와 패턴인덱스 길이가 같다! 면 패턴이 발견됨!
            yam += 1
            pi = 0

    print(f"#{tc} {yam}")
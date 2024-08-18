import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    string = [input() for _ in range(5)]

    scale = 0  # 문자열 중 가장 긴 길이 탐색
    for x in string:
        if len(x) > scale:
            scale = len(x)
    # 모든 문자열 길이 통일
    for i in range(5):
        if len(string[i]) != scale:
            new_range = scale - len(string[i])
            for _ in range(new_range):
                string[i] += "."
    # 세로 탐색하며 결과 만들기.
    result = ""
    for i in range(scale):
        for j in range(5):
            if string[j][i] == ".":
                pass
            else:
                result += string[j][i]

    print(f"#{tc} {result}")

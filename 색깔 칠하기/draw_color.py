import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input()) + 1

for tc in range(1, T):
    n = int(input())    # 첫 줄에 칠할 영역의 개수

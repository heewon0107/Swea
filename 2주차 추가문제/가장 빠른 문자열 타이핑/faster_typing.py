import sys
sys.stdin = open("sample_input.txt", "r")

tc = int(input())
for t in range(1, tc+1):
    A, B = input().split()  # A = 텍스트, B = 패턴
    # A는 텍스트, B는 패턴.
    pt = len(A) # 텍스트의 길이
    pl = len(B) # 패턴의 길이

    ti = 0  # 텍스트의 순회 인덱스
    pi = 0  # 패턴의 순회 인덱스

    if A[ti] != B[pi]:
        ti = ti - pi    #
        pi = -1

    ti += 1
    pi += 1
    if pl == pi:    # 패턴 발견

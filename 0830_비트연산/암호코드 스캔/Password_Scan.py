import sys

sys.stdin = open("sample_input.txt", "r")

to_bn = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111",
}

T = int(input())
for tc in range(1, 1+1):
    N, M = map(int, input().split())
    arr = list(input()[:M] for _ in range(N))
    code_lst = []

    for i in range(N):
        if int(arr[i], 16) and arr[i] not in code_lst:
            code_lst.append(arr[i])

    for code in code_lst:



import sys
sys.stdin = open("input.txt", "r")
#  simple factorization

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())    # num before factorization
    a = 0     # 2
    b = 0     # 3
    c = 0     # 5
    d = 0     # 7
    e = 0     # 11

    while n % 2 == 0:
        n = n / 2
        a += 1
    while n % 3 == 0:
        n = n / 3
        b += 1
    while n % 5 == 0:
        n = n / 5
        c += 1
    while n % 7 == 0:
        n = n / 7
        d += 1
    while n % 11 == 0:
        n = n / 11
        e += 1

    print(f"#{tc} {a} {b} {c} {d} {e}")
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())

    number = 12
    # 합이 6인 부분집합의 개수
    count = 0

    # 집합
    number_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # 원소의 개수가 n개 인 집합의 부분집합의 개수는 2^n
    # 2^n 번 반복해서 모든 부분집합의 합을 확인하자
    # 2^n == 1 << n
    # 시작을 1로 하면 공집합 제외
    for i in range(0, 1 << number):
        # i번째 부분집합의 합이 0인지 확인
        ith_subset_sum = 0
        ith_subset = []

        # i를 이진수로 바꿔서 생각해보자.
        # 이진수의 각 자릿수는 0 또는 1인데
        # 1인경우 => 그 자리수(인덱스)에 있는 원소를 골랐다고 생각하자
        # 0인경우 => 그 자릿수(인덱스)에 있는 원소를 고르지 않았다고 생각하자
        # 각 자릿수에 1이 있는지 없는지 어떻게 알아???
        # 이진수 1을 왼쪽으로 최대 n번 밀어 보면서 다 확인, 비트 & 연산을 사용
        # 왼쪽으로 0번 밀고, 1번 밀고, 2번 밀고, ... n-1번 까지 밀어보자.
        for j in range(number):  # :j : 왼쪽으로 밀어본 횟수
            if i & (1 << j) > 0:
                # i를 이진수로 만들었을 때 j번째 비트에 1이 있다.
                # j번 원소를 부분집합에 포함한 것으로 생각하겠따.
                ith_subset_sum += number_set[j]
                ith_subset.append(number_set[j])

        if ith_subset_sum == k and len(ith_subset) == n:
                # i번째 부분집합의 합이 k이면 1로 바꾸기(개수 구하는 문제면 +1)

                # ith_subset[i] = 1
            count += 1
            # print(ith_subset)
    print(f"#{tc} {count}")
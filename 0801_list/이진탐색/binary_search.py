import sys

sys.stdin = open("sample_input.txt", "r")

test_case = int(input())

def search_page(total, target_page):
    start = 1
    end = total    #  총 페이지를 끝 페이지로 할당
    count = 0      # 페이지를 반으로 쪼갠 횟수
    while start < end:
        mid = (start + end) // 2
        if target_page == mid:  # 고른 쪽이 target
            return count
        elif target_page < mid:  # target이 왼쪽에 있다.
            count += 1
            end = mid
        else:                   # target이 오른쪽에 있다.
            count += 1
            start = mid
for tc in range(1, test_case + 1):

    # total = 총 페이지 수
    # pa = a가 찾아야할 쪽
    # pb = b가 찾아야할 쪽
    total, pa, pb = map(int, input().split())
    pa_count = search_page(total, pa)  # A가 탐색한 횟수
    pb_count = search_page(total, pb)  # B가 탐색한 횟수

    if pa_count < pb_count:  # A가 빨리 찾았다.
        result = "A"
    elif pa_count > pb_count:  # B가 빨리 찾았다.
        result = "B"
    else:  # 무승부
        result = 0
    print(f"#{tc}", result)

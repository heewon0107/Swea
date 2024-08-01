test_case = 10

for tc in range(1, test_case + 1):
    n = int(input()) # 빌딩 수
    height = list(map(int, input().split())) # 빌딩 높이

    good_view = 0 # 조망권
    for i in range(2, n-2): # 빌딩 수 - 강물
        for j in range(height[i], -1, -1):
            height[i] = j
            if height[i] > height[i-1] and height[i] > height[i-2] and height[i] > height[i+1] and height[i] > height[i+2]:
                good_view += 1
            else:
                break
    print(f"#{tc} {good_view}")
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N = id의 개수
    id_lst = list(map(int, input().split()))    # 저장된 id 정보

    result = 0
    for i in range(N):
        result = id_lst[i] ^ result
    print(f"#{tc} {result}")
    
    # visited = [0] * 20001
    # for i in id_lst:
    #     # 음수면
    #     if i < 0:
    #         x = -i
    #         if not visited[x]:
    #             visited[x] = 1
    #         else:
    #             visited[x] = 0
    #     # 양수면
    #     else:
    #         x = i + 10000
    #         if not visited[x]:
    #             visited[x] = 1
    #         else:
    #             visited[x] = 0
    # for i in range(20001):
    #     if visited[i] == 1:
    #         if i < 10000:
    #             print(f"#{tc} {-i}")
    #             break
    #         else:
    #             print(f"#{tc} {i-10000}")
    #             break
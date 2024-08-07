import sys
sys.stdin = open("input.txt", "r")

# 길찾기 dfs 사용


# A = 0 , B = 99
#
          # 1 2 3 4 5 6 7 8 9 10 B
# adj_m = [[0,1,1,0,0,0,0,0,0,0,0,0],
#          [1,0,0,1,1,0,0,0,0,0,0,0],
#          [1,0,0,0,0,1,0,0,0,1,0,0],
#          [0,1,0,0,1,0,0,1,0,0,0,0],
#          [0,1,0,1,0,0,0,0,1,0,0,0],
#          [0,0,1,0,0,0,1,1,0,0,0,0],
#          [0,0,0,0,0,1,0,0,0,0,1,0],
#          [0,0,0,1,0,1,0,0,0,0,0,1],
#          [0,0,0,0,1,0,0,0,0,1,0,0],
#          [0,0,1,0,0,0,0,0,1,0,1,0],
#          [0,0,0,0,0,0,1,0,0,1,0,0],
#          [0,0,0,0,0,0,0,1,0,0,0,0],
#          ]
# def dfs_m(s, V):    # 1 16
#     # 방문체크
#     visited = [0] * V
#
#     # 스택 설정
#     stack = []
#
#     # 시작 정점은 방문 처리
#     visited[s] = 1
#
#     # 현재 방문하고 있는 정점
#     v = s
#
#     while True:
#         for i in range(0, V):
#             if adj_list[v][i] is not False: # 접근할 수 있으면.
#                 v = adj_list[v][i]  # 그 방으로 정점 이동
#                 stack.append(v)
#                 print(stack) # 스택을 쌓아준다.
#                 if v == 99:
#                     print(f"#{shop} 1 도착")
#                     break
#             else:       # 방이 비어있으면
#                 v = stack.pop() # 스택 줄어들고 전 방으로 간다.
#         else:   # break가 된적이 없으면.
#             print(f"#{shop} 0 길 없음")
#             break
#
#
test_case = 1
for tc in range(1, test_case +1):
    shop, V = map(int,input().split()) # s = 날리기, 간선 개수
    arr = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]
    for i in range(0, V*2, 2):
        v1, v2 = arr[i], arr[i+1]
        adj_list[v1].append(v2)

    # 탐색 시작

# dfs_m(0, V)

# ###########################
# test_case = 1
# for tc in range(1, test_case +1):
#
#     dfs_dict = {}
#     shop, V = map(int,input().split()) # s = 날리기, 간선 개수
#     arr = list(map(int, input().split()))
#     adj_list = [[] for _ in range(100)]
#     for i in range(0, V*2, 2):
#         v1, v2 = arr[i], arr[i+1]
#         if v1 in dfs_dict:
#             dfs_dict[v1].append(v2)
#         else:
#             dfs_dict[v1] = [v2]
#
#     print(dfs_dict)
#     # for i in range(100): # 100 번 까지의 길을 탐색한다.
#         x = 0   # 순회할 변수 할당.
#         position = 0
#         stack = []
#         while dfs_dict[x] != 99:    # 길을 찾으면 중단
#             v_len = len(dfs_dict[x])
#             if v_len > 0 :  # 딕셔너리의 밸류 값이 있다면
#                 for i in range(v_len):
#                     position = dfs_dict[x][i]    # 포지션을 변경해준다.
#                     stack.append(x)
#                     if len(dfs_dict[position]) > 0: # 새로운 길이 있으면
#                         x = position    # x에 포지션 할당.
#                         break
#                     else: # 길이 없으면
#                         x = stack.pop()


# 길찾기 dfs 사용
# A = 0 , B = 99
#
          # 1 2 3 4 5 6 7 8 9 10 B
adj_m = [[0,1,1,0,0,0,0,0,0,0,0,0],
         [1,0,0,1,1,0,0,0,0,0,0,0],
         [1,0,0,0,0,1,0,0,0,1,0,0],
         [0,1,0,0,1,0,0,1,0,0,0,0],
         [0,1,0,1,0,0,0,0,1,0,0,0],
         [0,0,1,0,0,0,1,1,0,0,0,0],
         [0,0,0,0,0,1,0,0,0,0,1,0],
         [0,0,0,1,0,1,0,0,0,0,0,1],
         [0,0,0,0,1,0,0,0,0,1,0,0],
         [0,0,1,0,0,0,0,0,1,0,1,0],
         [0,0,0,0,0,0,1,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,0,0,0,0],
         ]
def dfs_m(s, V):
    # 방문체크
    visited = [0]* (V+1)

    # 스택 설정
    stack = []

    # 시작 정점은 방문 처리
    visited[s] = 1

    # 현재 방문하고 있는 정점
    v = s

    while True:
        for i in range(1, V+1):
            if adj_m[v][]

import sys

sys.stdin = open("sample_input.txt", "r")

def tree(root):

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())    # E = 간선의 개수, N = 루트
    arr = list(map(int, input().split()))
    adj_lst = [[] for _ in range(E+2)]    # 인접리스트 번호
    left = []
    for i in range(0, E*2, 2):
        adj_lst[arr[i]].append(arr[i+1])
    # print(adj_lst)

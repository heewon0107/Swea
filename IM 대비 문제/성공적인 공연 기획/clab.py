import sys

sys.stdin = open("sample_input (1).txt", "r")

T = int(input())
for tc in range(1, T+1):
    clab_member = input()
    N = len(clab_member)
    hire_man = 0    # 고용해야 할 사람
    clab_num = 0    # 박수친 횟수

    for i in range(N):
        if clab_num < i:    # 박수친 횟수가 i 보다 작을 때
            hire_man += i - clab_num
            clab_num = i
        clab_num += int(clab_member[i])
    print(f"#{tc} {hire_man}")
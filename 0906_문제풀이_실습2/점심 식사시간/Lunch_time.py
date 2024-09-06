import sys

sys.stdin = open("sample_input.txt", "r")



# per[i] 0 = i, 1 = j, 2 = time, 3 = down
def stair(idx, jdx):
    global stair_1, stair_2
    # 1번 계단 가는 경우
    while person:
        for per in range(len(person)):
            # 계단에 도착하면
            if person[per][0] == stop[0][0] and person[per][1] == stop[0][1]:
                person[per][2] += 1
                person[per][3] += 1
                if person[per][3] == stop[0][3]:
                    stair_1 -= 1
                    result_time.add(person[per[2]])
                    person.pop(per)
                    continue
            # i 열 가기
            # 아래로
            if person[per][0] < stop[0][0]:
                person[per][0] += 1
                person[per][2] += 1
            # 위로
            elif person[per][0] > stop[0][0]:
                person[per][0] -= 1
                person[per][2] += 1
            # j열 가기
            # 우측
            if person[per][1] < stop[0][1]:
                person[per][1] += 1
                person[per][2] += 1
            # 좌측
            elif person[per][1] > stop[0][1]:
                person[per][1] -= 1
                person[per][2] += 1
            # 도착시 인원수 증가.
            else:
                # 계단 허용 인원
                if stair_1 < stop[0][2]:
                    stair_1 += 1
                # 허용 불가시 웨이팅
                else:
                    person[per][2] += 1

    # 2번 계단 가는 경우


# 계단은 반드시 두개
T = int(input())
for tc in range(1, 1 + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    person = []
    stop = []
    result_time = set()
    stair_1 = stair_2 = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                person.append((i, j, 0, 0))
            elif arr[i][j] > 1:
                stop.append((i, j, arr[i][j]))



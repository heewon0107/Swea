import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())    # n일 동안 수업 수강
    subject = list(map(int, input().split()))   # 특별 수업 열리는 날짜
    go_list = [0] * 7
    new_idx = 0
    min_val = 99999999999999999
    for i in range(7):
        go = 0  # 한 요일의 등교 횟수
        take = 0    # 특별 수업을 수강한 횟수
        # 수업 가는 첫 날 찾기
        idx = i
        while take < n:     # n 만큼의 수업을 들어야 함.
            go += 1         # 학교에 등교했어.
            if subject[idx] == 1:   # 특별수업을 들으면 take +1
                take += 1
                if take == n:
                    go_list[i] = go
                    # 수강 끝
                    break
            idx += 1    # 다음 수업 준비
            if idx > 6:     # 일주일은 0~6의 인덱스를 가짐.
                idx = 0

        # if go < min_val:
        #     min_val = go
        #     new_idx = idx
    # 최적의 요일로 실행
    # take = 0
    # result = 0
    # while take < n:
    #     result += 1                 # 등교 횟수
    #     if subject[new_idx] == 1:   # 수업 듣고
    #         take += 1
    #         if take == n:
    #             break
    #     new_idx += 1
    #     if new_idx > 6:
    #         new_idx = 0

    print(f"#{tc} {min(go_list)}")

import sys
sys.stdin = open("sample_input.txt", "r")

test_case = int(input())
for tc in range(1, test_case+1):
    k, n, m = map(int, input(). split())   # k = 충전기 용량, n = 출발점 0부터 종점까지의 거리, m = 충전소 개수
    charge_list = list(map(int, input(). split()))  # 충전소 번호
    charge_amount = k   # 현재 배터리 상태
    car_position = 0    # 차량의 위치
    charge_time = 0     # 충전 횟수

    while car_position < n:     # 차량의 위치가 종점일 때 종료.

        if charge_amount >= n - car_position:    # 종점까지 갈 수 있는 배터리 상태 양호
            car_position = n   # 도착

        else:
            for j in range(charge_amount, 0, -1):    # 배터리 용량 내에서 충전소 찾기

                if (car_position + j) in charge_list:   # 충전소 뒤에서부터 찾기
                    car_position += j   # 충전소까지 주행
                    charge_time += 1    # 충전 횟수 +1
                    break
                if j == 1:
                    charge_time == 0
                    car_position = n
                    break
    print(f"#{tc} {charge_time}")

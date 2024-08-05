t = 10

for tc in range(1, t + 1):
    input()

    p = input()
    t = input()

    count = 0

    pl = len(p)  # 패턴길이
    tl = len(t)  # 텍스트 길이

    pi = 0  # 패턴 전용 인덱스
    ti = 0  # 텍스트 전용 인덱스

    while pi < pl and ti < tl:
        # p[pi]와 t[ti] 를 비교해서
        # 같다? pi, ti +1
        # 다르다? 앞으로 돌아가서 다시 비교

        # 다르면 앞으로 돌아가기
        if t[ti] != p[pi]:
            # 다음 비교 시작 위치 = 현재 비교 위치 - 내가 비교한 횟수
            # 텍스트 비교 시작 위치 = ti - pi
            ti = ti - pi
            # 패턴 비교 시작 위치 = -1
            pi = -1
        # 다음 비교 위치로 이동 +1
        pi += 1
        ti += 1

        # pi 가 패턴의 길이만큼 되어버렸다면??
        # 중간에 달랐던 적이 없었다. > 패턴을 발견했다!
        if pi == pl:
            count += 1

            # 다음 비교를 위해서 다음 비교 시작 위치로 이동
            ti = ti - pi + 1
            pi = 0  # -1 + 1
    print(f"#{tc} {count}")
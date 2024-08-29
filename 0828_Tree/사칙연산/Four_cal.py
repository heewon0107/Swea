def last_order(node):
    if node == 0:
        return

    # 정점이 사칙 연산 기호에 맞게 서브트리들을 연산해줌.
    x = tree[node]
    if x == "+":
        return last_order(left[node]) + last_order(right[node])
    elif x == "-":
        return last_order(left[node]) - last_order(right[node])
    elif x == "/":
        return last_order(left[node]) / last_order(right[node])
    elif x == "*":
        return last_order(left[node]) * last_order(right[node])
    else:   # 숫자면 사칙연산 기호 찾아 순회
        last_order(left[node])
        last_order(right[node])
        return x
T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(N):
        node = i + 1
        arr = input().split()
        if len(arr) > 2:
            tree[node], left[node], right[node] = arr[1], int(arr[2]), int(arr[3])
        else:
            tree[node] = int(arr[1])
    result = int(last_order(1))
    print(f"#{tc} {result}")
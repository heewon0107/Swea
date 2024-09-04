def quick(l, r):
    p = arr[l]
    i = l
    j = r

    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = quick(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

arr = list(map(int, input().split()))
N = len(arr)
quick_sort(0, N-1)
print(arr[500000])
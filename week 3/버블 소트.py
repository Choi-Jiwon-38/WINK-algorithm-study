def bubble_sort(arr):
    swap_count = 0
    end = n - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
                swap_count += 1
        end = last_swap
    print(swap_count)

n = int(input())
arr = list(map(int, input().split()))
bubble_sort(arr)
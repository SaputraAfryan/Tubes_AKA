def combSort(arr):
    gap = n = len(arr)
    swapped = True

    while gap > 1 or swapped:
        swapped = False
        gap = int(gap * 10 / 13)

        if gap < 1:
            swapped = False
            gap = 1

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr


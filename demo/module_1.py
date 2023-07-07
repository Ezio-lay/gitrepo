def choose_sort(arr: list):
    l = len(arr) - 1
    while l > 0:
        index = 0
        for i in range(l + 1):
            if arr[i] > arr[index]:
                index = i
        arr[index], arr[l] = arr[l], arr[index]
        l -= 1
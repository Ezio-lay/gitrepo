def choose_sort(arr: list):
    l = len(arr) - 1
    while l > 0:
        index = 0
        for i in range(l + 1):
            if arr[i] > arr[index]:
                index = i
        arr[index], arr[l] = arr[l], arr[index]
        l -= 1


def insert_sort(arr: list):
    l = len(arr)
    i = 0
    while i < l - 1:
        j = i + 1
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
            else:
                break
        i += 1
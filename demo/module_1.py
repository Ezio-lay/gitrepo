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


def quick_sort(arr: list, begin, end):
    if begin >= end:
        return
    key = arr[begin]
    left = hole = begin
    right = end
    while left < right:
        while arr[right] > key and left < right:
            right -= 1
        arr[hole] = arr[right]
        hole = right
        while arr[left] < key and left < right:
            left += 1
        arr[hole] = arr[left]
        hole = left
    arr[hole] = key
    quick_sort(arr, begin, left - 1)
    quick_sort(arr, left + 1, end)

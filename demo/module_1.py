def bubble_arr(arr: list):
    l = len(arr)
    while l > 1:
        i = 1
        while i < l:
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i += 1
        l -= 1


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


def count_sort(arr: list):
    t = [0] * (max(arr) + 1)
    for x in arr:
        t[x] += 1
    arr.clear()
    for x in range(len(t)):
        for y in range(t[x]):
            arr.append(x)


def base_sort(arr: list):
    l = len(str(max(arr)))
    i = 0
    while i < l:
        bucket = [[] for _ in range(10)]
        for x in arr:
            bucket[x // (10 ** i) % 10].append(x)
        arr.clear()
        for x in bucket:
            for y in x:
                arr.append(y)
        i += l


def bucket_sort(arr: list):
    num = (max(arr) - min(arr)) // 3 + 1
    bucket = [[] for _ in range(num)]
    for x in arr:
        bucket[(x - min(arr)) // 3].append(x)
    print(bucket)
    for x in bucket:
        x.sort()
    arr.clear()
    for x in bucket:
        for y in x:
            arr.append(y)


def heap_sort(arr, n):
    if n == 1:
        return
    tar = n // 2 - 1
    while tar >= 0:
        r = 2 * tar + 2
        l = 2 * tar + 1
        if r > n - 1:
            if arr[l] > arr[tar]:
                arr[l], arr[tar] = arr[tar], arr[l]
        else:
            if arr[l] == max(arr[tar], arr[l], arr[r]):
                arr[l], arr[tar] = arr[tar], arr[l]
            elif arr[r] == max(arr[tar], arr[l], arr[r]):
                arr[r], arr[tar] = arr[tar], arr[r]
        tar -= 1
    arr[0], arr[n - 1] = arr[n - 1], arr[0]
    heap_sort(arr, n - 1)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            temp = arr[j]
            while j >= gap and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j = j - gap
        gap = gap // 2




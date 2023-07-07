# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from demo.module_1 import *


def sort_arr(arr: list):
    l = len(arr)
    while l > 1:
        i = 1
        while i < l:
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i += 1
        l -= 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [6, 1, 4, 3, 2]
    insert_sort(a)
    print(a)
    print('End')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

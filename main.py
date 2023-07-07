# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from demo.module_1 import *
import random


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append(random.randint(0, 100))
    print(a)
    shell_sort(a)
    print(a == sorted(a))
    print(a)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

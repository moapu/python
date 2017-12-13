import timeit


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


alist = [13, 43, 26, 28, 89, 70, 23, 24, 11, 8, 91]
bubbleSort(alist)
print(alist)
print(timeit.timeit())

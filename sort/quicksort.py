# In place quick sort which is also the default sort algorithm of python

import random
import time


def quicksort(lst, head, tail):
    if head < tail:
        p = partition(lst, head, tail)
        quicksort(lst, head, p)  # do it recursively
        quicksort(lst, p+1, tail)  # do it recursively
    return lst


def partition(lst, head, tail):
    pivot = lst[tail-1]  # Choose pivot from tail, so we don't need space n to store temp value
    i = head - 1
    # Put lst[j] < pivot to the left iteratively, by exchange lst[i] and lst[j]
    for j in range(head, tail):
        if lst[j] < pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[tail-1] < lst[i+1]:
        lst[i+1], lst[tail-1] = lst[tail-1], lst[i+1]   # Exchange pivot with lst[i+1]
    return i+1 # return the index of sorted sub-list

a = []
for size in range(50):
    a.append(random.randint(1,100))
print(a)
b = quicksort(a, 0, len(a))
print(b)
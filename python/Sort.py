#! /usr/bin/python
# coding=utf8

import sys
import time
import random

def select_sort(data_list):
    print("starting select sorting........")
    begin_time = time.time()
    n = len(data_list)
    for i in range(n):
        k = i
        is_sorted = True
        for j in range(i+1, n):
            if data_list[j] < data_list[k]:
                k = j
            if data_list[j] < data_list[j-1]:
                is_sorted = False
        if is_sorted:
            break
        if k != i:
            data_list[i], data_list[k] = data_list[k], data_list[i]
    print("elasped time: {} seconds".format(time.time()-begin_time))
    print("select sort result: ")
    print(data_list)


def bubble_sort(data_list):
    print("starting bubble sorting........")
    begin_time = time.time()
    n = len(data_list)
    for i in range(n-1, -1, -1):
        is_swaped = False
        for j in range(0, i):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
                is_swaped = True
        if not is_swaped:
            break
    print("elasped time: {} seconds".format(time.time()-begin_time))
    print("bubble sort result: ")
    print(data_list)


def insert_sort(data_list):
    print("starting insert sorting........")
    begin_time = time.time()
    n = len(data_list)
    for i in range(1, n):
        i_value = data_list[i]
        k = i
        for j in range(i-1, -1, -1):
            if data_list[j] > i_value:
                data_list[j+1] = data_list[j]
                k = j
            else:
                break
        if k != i:
            data_list[k] = i_value
    print("elasped time: {} seconds".format(time.time()-begin_time))
    print("insert sort result: ")
    print(data_list)


def quick_sort(data_list, left, right):
    if left < right:
        p = partition(data_list, left, right)
        quick_sort(data_list, left, p)
        quick_sort(data_list, p+1, right)


def partition(data_list, left, right):
    pivot = data_list[(left + right) / 2]
    i = left
    j = right
    while True:
        while data_list[i] < pivot:
            i += 1
        while data_list[j] > pivot:
            j -= 1
        if i >= j:
            return j
        data_list[i], data_list[j] = data_list[j], data_list[i]


if __name__ == '__main__':
    n = int(sys.argv[1])
    data_list = [random.randint(1, 10000) for i in range(n)]
    # data_list.sort(reverse=True)
    print("source data list: ")
    print(data_list)
    select_data_list = list(data_list)
    select_sort(select_data_list)
    print("")
    bubble_data_list = list(data_list)
    bubble_sort(bubble_data_list)
    print("")
    insert_data_list = list(data_list)
    insert_sort(insert_data_list)
    print("")
    quick_data_list = list(data_list)
    print("starting quick sorting........")
    begin_time = time.time()
    quick_sort(quick_data_list, 0, n-1)
    print("elasped time: {} seconds".format(time.time()-begin_time))
    print("quick sort result: ")
    print(quick_data_list)
    print("")
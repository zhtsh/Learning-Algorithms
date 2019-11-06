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


if __name__ == '__main__':
    n = int(sys.argv[1])
    data_list = [random.randint(1, 10000) for i in range(n)]
    select_data_list = list(data_list)
    select_sort(select_data_list)
    print("")
    bubble_data_list = list(data_list)
    bubble_sort(bubble_data_list)
    print("")
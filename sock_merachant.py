#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    item_count = {}
    for item in ar:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    for each_key in item_count:
        item_count[each_key] = item_count[each_key] // 2
    return sum(item_count.keys())

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)

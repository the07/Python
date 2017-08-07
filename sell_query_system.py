#!/bin/env/python3

import sys

sold_list = {}

def add_to_sell(item):
    """Code to add items to the sold list, which is a dictonary"""
    if item[0] not in sold_list:
        sold_list[item[0]] = []
        sold_list[item[0]].append(item[1:])
    else:
        sold_list[item[0]].append(item[1:])

def query(item):
    """Code to search for a given item from the sold list"""
    sorted_date = sorted(sold_list.keys())
    count = 0
    if item[0] in sorted_date:
        products_sold_on_date = sold_list[item[0]]
        for each_product in products_sold_on_date:
            if item[1] == each_product[0] and item[2] == each_product[1]:
                count += 1
    return count

T = int(input().strip())
while T:
    user_input = list(input().split(' '))
    if user_input[0] == 'Q':
        print (query(user_input[1:]))
    else:
        add_to_sell(user_input[1:])
    T -= 1

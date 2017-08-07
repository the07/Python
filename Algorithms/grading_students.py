#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    new_grades = []
    for each_grade in grades:
        if each_grade >= 38:
            if each_grade % 5 >= 3:
                each_grade = each_grade + ( 5 - (each_grade % 5))
        new_grades.append(each_grade)
    return new_grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))

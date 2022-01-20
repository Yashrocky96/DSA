"""
Using comparator functions to solve complex sorting
cmp is depreciated in 3.x python, it was moved to functools module
"""

import functools


# Writing comparator function

def sortStruct(x, y):
    s1 = sum(x[2:])
    s2 = sum(y[2:])

    # No swap
    if s1 > s2:
        return 1
    # Swap
    elif s1 < s2:
        return -1
    # Compare names when marks are same
    elif s1 == s2:
        # x name is greater means alphabetically great, no swap
        if x[1].lower() < y[1].lower():
            return 1
        # Swap
        elif x[1].lower() > y[1].lower():
            return -1 
        # All other cases meaning names are same?
        else:
            # Compare based on ID, if greater then no swap
            if x[0] > y[0]:
                return -1
            #Swap cause of reverse parameter
            else:
                return 1
    

def marksSort(n, students):
    students.sort(key = functools.cmp_to_key(sortStruct), reverse=True)
    res = [i[0] for i in students]
    return res

def main():
    n = int(input())
    students = []
    for i in range(n):
        student = input().split()
        for j in range(7):
            if j != 1:
                student[j] = int(student[j])
        students.append(student)

    result = marksSort(n, students)
    print(*result)

if __name__=="__main__":
    main()
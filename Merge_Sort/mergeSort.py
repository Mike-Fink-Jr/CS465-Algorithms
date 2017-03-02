import sys


def merge(left, right):
    x = 0
    final = []
    y = 0
    while x < len(left) and y < len(right):
        if left[x] > right[y]:
            final.append(right[y])
            y += 1
        else:
            final.append(left[x])
            x += 1

    final += left[x:]
    final += right[y:]
    return final
    pass


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)
    pass
while False:
    # Read input
    n = [int(i) for i in sys.stdin.readline().split()][0]
    numbers = [int(i) for i in sys.stdin.readline().split()]

    compCount = merge_sort(numbers)

    print ' '.join(str(i) for i in compCount)


import sys


def sort(numbers):
    n = len(numbers)-1
    count = 0
    i=0
    while i<n:
        temp = i + 1

        count += 1

        curr = numbers[temp]

        while numbers[temp - 1] > curr and temp>0:
            count += 1
            numbers[temp] = numbers[temp-1]
            temp -=1
    #    print temp,numbers[temp],numbers,curr
    #    print temp, numbers
        i += 1
        numbers[temp] = curr


    return count


# Reading the input from the stdin
n = [int(x) for x in sys.stdin.readline().split()][0]
number = [int(x) for x in sys.stdin.readline().split()]
# Sorting the numbers and keeping track of the number of comparisons performed in the process
compCount = sort(number)
# Printing the result
print(compCount)
print ' '.join(str(x) for x in number)


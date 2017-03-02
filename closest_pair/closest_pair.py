#in a given set of points uniformly distributed on the (x,y) plane
#this algorithm finds the closest pair of points in O(n) 


import sys
import math
import random


# For a list of input points, returns a pair with the minimum Euclidean distance
def sameCell(pointList):

    index = 0
    n = len(pointList)
    minDist = 10000000.0
    for i in pointList:
        x1, y1 = i
        index += 1
        for j in xrange(index, n):
            x2, y2 = pointList[j]
            xDist, yDist = x1 - x2, y1 - y2
            currDist = xDist * xDist + yDist * yDist
            if currDist < minDist:
                minDist = currDist
                A = i
                B = pointList[j]
    return [A, B, minDist]


"""
Takes a point from one cell (x1, y1) and all points from three
of its neighbouring cells and returns the closest point from (x1, y1)
"""


# neighbours contains points from three different cells, but can be treated as a single list
def neighbourCell(point, neighbours):

    minDist = 100000.0
    x1, y1 = point
    closestPt = []
    for num in neighbours:
        x2, y2 = num
        xDist, yDist = x1 - x2, y1 - y2
        currDist = xDist * xDist + yDist * yDist
        if currDist < minDist:
            minDist = currDist
            closestPt = num
    return [closestPt, minDist]


def findClosestPair(points):
    n = len(points)
    if n == 0:
        return []
    gridSize = int(math.floor(math.sqrt(n)))

    cells = [None] * gridSize * gridSize  # Initialize an empty list of size txt

    for j in xrange(len(cells)):
        cells[j] = []  # Initializing all list elements to an empty nested list

    for i in points:
        x = int(math.floor(gridSize * i[0]))  # x co-ordinate
        y = int(math.floor(gridSize * i[1]))  # y co-ordinate
        if i[0] == 1.0:
            x -= 1
        if i[1] == 1.0:
            y -= 1

        cells[gridSize * x + y].append(i)


    if len(cells) == 1:
        iterations = 1
    else:
        iterations = len(cells) - gridSize - 1

    minDist = 100000.0
    minPoints = [(0.0, 0.0), (0.0, 0.0)]

    for k in xrange(iterations):
        if len(cells[k]) > 1:
            minSame = sameCell(cells[k])
            minSamePoints = (minSame[:2])
            minSameDist = minSame[-1]
            if (minSameDist < minDist) and (minSameDist != 0.0):
                minDist = minSameDist
                minPoints = minSamePoints

        # if iterations > 1:
        if len(cells) > 1:
            for l in xrange(len(cells[k])):
                minNeighbour = neighbourCell(cells[k][l], cells[k + 1] + cells[k + gridSize] + cells[k + 1 + gridSize])
                minNeighbourPoints = [cells[k][l], minNeighbour[0]]
                minNeighbourDist = minNeighbour[1]
                if minNeighbourDist < minDist:
                    minDist = minNeighbourDist
                    minPoints = minNeighbourPoints

    # For cells at the edge of the grid
    # The right vertical edge
    for edge in xrange(gridSize - 1, gridSize * gridSize - 1, gridSize):
        if len(cells[edge]) > 1:
            minSame = sameCell(cells[edge])
            minSamePoints = (minSame[:2])
            minSameDist = minSame[-1]
            # if minSameDist < minDist:
            if (minSameDist < minDist) and (minSameDist != 0.0):
                minDist = minSameDist
                minPoints = minSamePoints
        for pt in xrange(len(cells[edge])):
            minNeighbour = neighbourCell(cells[edge][pt], cells[edge + gridSize])
            minNeighbourPoints = [cells[edge][pt], minNeighbour[0]]
            minNeighbourDist = minNeighbour[1]

            if minNeighbourDist < minDist:
                minDist = minNeighbourDist
                minPoints = minNeighbourPoints

    # The top horizontal edge
    for edge in xrange(gridSize * (gridSize - 1), gridSize * gridSize - 1, 1):
        if len(cells[edge]) > 1:
            minSame = sameCell(cells[edge])
            minSamePoints = (minSame[:2])
            minSameDist = minSame[-1]
            # if minSameDist < minDist:
            if (minSameDist < minDist) and (minSameDist != 0.0):
                minDist = minSameDist
                minPoints = minSamePoints

            minNeighbour = neighbourCell(cells[edge][pt], cells[edge + 1])
            minNeighbourPoints = [cells[edge][pt], minNeighbour[0]]
            minNeighbourDist = minNeighbour[1]
            if minNeighbourDist < minDist:
                minDist = minNeighbourDist
                minPoints = minNeighbourPoints

    # Another case: for diagonally top left
    for num in xrange(gridSize * (gridSize - 1)):
        if num % gridSize:
            for pt in xrange(len(cells[num])):
                minNeighbour = neighbourCell(cells[num][pt], cells[num + gridSize - 1])
                minNeighbourPoints = [cells[num][pt], minNeighbour[0]]
                minNeighbourDist = minNeighbour[1]
                if minNeighbourDist < minDist:
                    minDist = minNeighbourDist
                    minPoints = minNeighbourPoints

    # Last case
    if len(cells[-1]) > 1:
        minSame = sameCell(cells[-1])
        minSamePoints = (minSame[:2])
        minSameDist = minSame[-1]

        if (minSameDist < minDist) and (minSameDist != 0.0):
            minDist = minSameDist
            minPoints = minSamePoints

    return minPoints


n = [int(x) for x in sys.stdin.readline().split()][0]
points = []
for i in xrange(n):
    x, y = [float(x) for x in sys.stdin.readline().split()]
    points.append((x, y))

closestPair = findClosestPair(points)

coords = []
for x, y in closestPair:
    coords.append(round(x, 6))
    coords.append(round(y, 6))

print ' '.join("%.6f" % x for x in coords)

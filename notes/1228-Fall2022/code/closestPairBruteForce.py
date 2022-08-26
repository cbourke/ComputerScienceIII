
import math
import random

def getRandomPoints(n):
    points = []
    for i in range(n):
        points.append( (random.randint(-1000000000, 1000000000),
                        random.randint(-1000000000, 1000000000) ) )
    return points

n = 1000000
pts = getRandomPoints(n)
minDist = math.inf
numComps = 0

for i in range(n-1):
    for j in range(i+1, n):
        (x1,y1) = pts[i]
        (x2,y2) = pts[j]
        dist = math.sqrt( (x1-x2) * (x1-x2) + (y1-y2)*(y1-y2))
        #print(f"comparing ({x1},{y1}) and ({x2}, {y2}): distance = {dist}")
        numComps += 1
        if dist < minDist:
            minDist = dist
            closestPair = ( (x1,y1), (x2,y2) )

print("Found closest pair: ")
print(closestPair)
print("num comps = " + str(numComps))

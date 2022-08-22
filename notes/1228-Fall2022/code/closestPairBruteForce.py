
import math
import random

def getRandomPoints(n):
    points = []
    for i in range(n):
        points.append( (random.randint(-1000000000, 1000000000), random.randint(-1000000000, 1000000000) ) )
    return points

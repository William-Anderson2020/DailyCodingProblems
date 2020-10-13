"""
A competitive runner would like to create a route that starts and ends at his
house, with the condition that the route goes entirely uphill at first, and then
entirely downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary
mapping paths between some of these locations to their corresponding distances,
find the length of the shortest route satisfying the condition above. Assume the
runner's home is location 0.

For example, suppose you are given the following input:

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
(0, 1): 10,
(0, 2): 8,
(0, 3): 15,
(1, 3): 12,
(2, 4): 10,
(3, 4): 5,
(3, 0): 17,
(4, 0): 10
}

In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance
of 28.
"""

def pathFinder(elevations, paths, initPos):
    #paths[0] = cur pos
    #paths[1] = path el
    #paths[i] val = path length
    newPath = [initPos]
    bounding = "up"
    def subRoute(path, b):
        curPos = newPath[-1]
        nextPos, nextDist = [0, 0]
        boundCheck = []
        for i in paths:
                if i[0] == curPos:
                    boundCheck.append(elevations[i[1]])
        if max(boundCheck) < elevations[curPos]:
            bounding = "down"
        
        for i in paths:
            if i[0] == curPos:
                if b == "up":
                    comparator = True
                else:
                    comparator = False
                print(nextDist)
                if (elevations[i[1]] > elevations[i[0]]) == comparator and (nextDist > paths[i] or nextDist == 0):
                    #print("FIRE")
                    nextPos, nextDist = [i[1], paths[i]]
        return nextPos
    while initPos not in newPath[1:]:
        newPath += [subRoute(newPath, bounding)]
    return newPath                



t1e = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
t1p = {
(0, 1): 10,
(0, 2): 8,
(0, 3): 15,
(1, 3): 12,
(2, 4): 10,
(3, 4): 5,
(3, 0): 17,
(4, 0): 10
}

print(pathFinder(t1e, t1p, 0))
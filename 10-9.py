"""
An imminent hurricane threatens the coastal town of Codeville. If at most two
people can fit in a rescue boat, and the maximum weight limit for a given boat
is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat
limit of 200, the smallest number of boats required will be three.

"""
import math
def evac(people):
    minBoats = 0
    i = 0
    while len(people) > 0:
        p1 = 0
        mWeight = 0
        boarding = [0,0]
        for p2 in range(len(people)):
            if p1 != p2:
                weight = people[p1] + people[p2]
                #print(p1,p2,weight)
                if weight > mWeight and weight <= 200:
                    mWeight = weight
                    boarding = [p1, p2]
                    #print("m",weight,mWeight)
        #print("l1",people,boarding)
        del people[boarding[1]]
        if boarding[1] != boarding[0]:
            del people[boarding[0]]
        minBoats += 1
        i += 1
        #print("l2",people)
    print("At least {} boats are required.".format(minBoats))
                
evac([100,120,100,150,50,60])

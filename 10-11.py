"""
You have N stones in a row, and would like to create from them a pyramid. This
pyramid should be constructed such that the height of each stone increases by
one until reaching the tallest stone, after which the heights decrease by one.
In addition, the start and end stones of the pyramid should each be one stone
high.

You can change the height of any stone by paying a cost of 1 unit to lower its
height by 1, as many times as necessary. Given this information, determine the
lowest cost method to produce this pyramid.

For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay
2 to create [0, 1, 2, 3, 2, 1].
"""

def pyramid(stones):
    nums = {"counts": {}, "spares": {}}
    cost = 0
    def count(num):
        c = 0
        for i in stones:
            if i == num:
                c += 1
        return c
    
    def repeater(value, ammount, l):
        i = 0
        while i < ammount:
            l.append(value)
            i+=1
    
    maxH = max(stones)
    
    for i in range(maxH + 1):
        nums["spares"][i] = count(i)%2
        nums["counts"][i] = count(i) - count(i)%2
        if i == max(stones):
            if count(i)%2 == 0 and count(i) > 1:
                nums["spares"][i] = 1
            if count(i) == 1:
                nums["spares"][i] = 0
            nums["counts"][i] = count(i) - nums["spares"][i]
    
    stackA = []
    stackB = []
    mid = []
    stackZ = []
    
    for i in nums["spares"]:
        v = nums["spares"][i]
        print(i,v)
        if v == 1:
            print("one")
            if nums["spares"][i-1] == 1:
                num["counts"][i-1] += 2
                num["spares"][i-1] = 0
                num["spares"][i-1] = 0
                cost += 1
            elif nums["spares"][i+1] == 1:
                num["counts"][i+1] += 2
                num["spares"][i+1] = 0
                num["spares"][i+1] = 0
                cost += 1
        elif i == 1 and v == 0 and nums["counts"][i] > 2:
            print("fire")
            if nums["spares"][2] == 1:
                nums["spares"][2] = 0
                nums["counts"][1] -= 2
                nums["counts"][2] += 2
                cost += 1
        elif i == max(stones) and v > 1:
            print("max")
            if nums["spares"][i-1] == 1:
                nums["spares"][i] = 0
                nums["spares"][i-1] = 0
                nums["counts"][i-1] += 2
                cost += 1
                
        
    
    for i in nums["counts"]:
        v = nums["counts"][i]
        if i == max(stones):
            repeater(i, v, mid)
        elif i == 0:
            repeater(i, v, stackZ)
        else:
            repeater(i, v/2, stackA)
            repeater(i, v/2, stackB)
    stackB.reverse()
    final = stackZ + stackA + mid + stackB
    
    return "The order will be {} at a cost of {}.".format(final,cost)
    
    
print(pyramid([1, 1, 3, 3, 2, 1, 1, 5]))


    
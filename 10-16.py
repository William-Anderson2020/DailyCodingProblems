"""
This problem was asked by Google.

A girl is walking along an apple orchard with a bag in each hand. She likes to
pick apples from each tree as she goes along, but is meticulous about not
putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in
order, determine the length of the longest portion of her path that consists of
just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will
involve types 1 and 3, with a length of four.

"""

def twoTypeLen(path):
    path.append("")
    checkedA = []
    count = 0
    types = []
    curS = []
    for t1 in path:
        if t1 not in checkedA:
            checkedB = []
            for t2 in path:
                if t1 != t2 and t2 not in checkedB:
                    subCount = 0
                    aString = []
                    for a in path:
                        aString.append(a)
                        if a == t1 or a == t2:
                            subCount += 1
                            curS.append(a)
                        else:
                            if subCount > count:
                                count = subCount
                                types = [t1,t2]
                            subCount = 0
                            curS = []
                    #print(aString)
                    checkedB.append(t2)
        checkedA.append(t1)
        
    return count
                    

testP = [2, 1, 2, 3, 3, 1, 3, 5, 3, 5, 3]
print(twoTypeLen(testP))
            
            
            
            
            
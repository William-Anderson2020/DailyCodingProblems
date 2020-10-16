"""
This problem was asked by Amazon.

At a popular bar, each customer has a set of favorite drinks, and will happily
accept any drink among this set. For example, in the following situation,
customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
0: [0, 1, 3, 6],
1: [1, 4, 7],
2: [2, 4, 7, 5],
3: [3, 2, 5],
4: [5, 8]
}

A lazy bartender working at this bar is trying to reduce his effort by limiting
the drink recipes he must memorize. Given a dictionary input such as the one
above, return the fewest number of drinks he must learn in order to satisfy all
customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy
everyone.

"""

def menu(prefs):
    mL = []
    #served = []
    def mostFreq(dL):
        superList = []
        drinkDict = {}
        for i in dL:
            superList += dL[i]
        for d in superList:
            if d not in drinkDict:
                drinkDict[d] = 0
            drinkDict[d] += 1
        cF = [-1,0]
        for f in drinkDict:
            if drinkDict[f] > cF[1]:
                cF = [f, drinkDict[f]]
        return cF
    while len(prefs) > 0:
        mL.append(mostFreq(prefs)[0])
        c = 0
        l = len(prefs)
        while c < l:
            for d in mL:
                if d in prefs[c]:
                    prefs.pop(c, None)
            c+=1
    return mL

            



preferences = {
0: [0, 1, 3, 6],
1: [1, 4, 7],
2: [2, 4, 7, 5],
3: [3, 2, 5],
4: [5, 8]
}

print(menu(preferences))
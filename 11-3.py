"""
You are given a circular lock with three wheels, each of which display the
numbers 0 through 9 in order. Each of these wheels rotate clockwise and
counterclockwise.

In addition, the lock has a certain number of "dead ends", meaning that if you
turn the wheels to one of these combinations, the lock becomes stuck in that
state and cannot be opened.

Let us consider a "move" to be a rotation of a single wheel by one digit, in
either direction. Given a lock initially set to 000, a target combination, and a
list of dead ends, write a function that returns the minimum number of moves
required to reach the target state, or None if this is impossible.

"""

def lockPick(target,trapsInit):
    moveCount = [0]
    combo = [0 for x in range(len(str(target)))]
    traps = []
    for x in trapsInit:
        traps.append([int(y) for y in str(x)])
    target = [int(x) for x in str(target)]
    def increase(num):
        for i in range(len(target)):
            if combo[i] != target[i]:
                combo[i]+=1
                if combo in traps:
                    combo[i]-=1
                    moveCount[0] += 1
                    continue
                moveCount[0]+=1
                print(combo,target,moveCount)
    while combo != target:
        increase(combo)
    print(traps)    
    return moveCount

print(lockPick(3241,[2901,1111,3301]))
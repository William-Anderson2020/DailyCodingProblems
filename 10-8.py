"""
On a mysterious island there are creatures known as Quxes which come in three
colors: red, green, and blue. One power of the Qux is that if two of them are
standing next to each other, they can transform into a single creature of the
third color.

Given N Quxes standing in a line, determine the smallest number of them
remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up
with a single Qux through the following steps:

Arrangement | Change

['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B'] | (B, G) -> R
['B', 'R', 'B'] | (R, B) -> G
['B', 'G'] | (B, G) -> R
['R'] |
"""

def merge(q1, q2):
    qs = ['R', 'G', 'B']
    for i in [q1, q2]:
        if i in qs:
            qs.remove(i)
    if len(qs) == 1:
        return qs
    else:
        return [q1, q2]

def quxes(list):
    i = 0
    changes = False
    while i < len(list)-1:
        c = merge(list[i], list[i+1])
        list = list[:i] + c + list[i+2:]
        if len(c) == 1:
            changes = True
        i+=1
    if changes == True:
        print("Loop", list)
        quxes(list)
    else:
        print("Return", list)
        return list

print(quxes(['R', 'G', 'B', 'G', 'B', 'B', 'R', 'G']))
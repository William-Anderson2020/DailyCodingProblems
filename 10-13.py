"""
Pascal's triangle is a triangular array of integers constructed with the
following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly
above it, on either side.
For example, here are the first few rows:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Given an input k, return the kth row of Pascal's triangle.
"""

def pascal(k):
    triangle = [[0,1,0]]
    bottomRow = [0,1,0]
    for i in range(k-1):
        newRow = [0]
        for n in range(len(bottomRow)-1):
            newRow.append(bottomRow[n]+bottomRow[n+1])
        newRow.append(0)
        bottomRow = newRow
    return bottomRow[1:-1]

print(pascal(5))
    
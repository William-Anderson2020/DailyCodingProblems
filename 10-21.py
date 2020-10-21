"""
This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree, the angle
between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
"""

def angle(time):
    hourHand,minuteHand = time.split(":")
    hourHand,minuteHand = int(hourHand),int(minuteHand)
    hourPlacement = hourHand * 5
    minutesBetween = abs(hourPlacement - minuteHand)
    degreesBetween = minutesBetween * 6
    if degreesBetween > 180:
        degreesBetween -= 180
    return degreesBetween
    
    
    
print(angle("12:45"))
"""Angle will be zero whenever the hour*5 = minutes or 12:00"""
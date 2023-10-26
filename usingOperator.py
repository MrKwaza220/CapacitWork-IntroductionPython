import math
numbers = 9.848787387
roundNumbers=round(numbers)
print(roundNumbers)

print("Enter number of litres:" )
numberOfLitres = float(input())
numberOfBottles = numberOfLitres / 0.5
remainingLitres = numberOfBottles % 0.5

print( numberOfLitres,"L water will fill", math.trunc(numberOfBottles),"bottles",round(remainingLitres),"Litres remains")

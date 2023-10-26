print("How many milimeters of water were released? ")
releasedWaterInMillilitres = float(input())

releasedWaterInLitres = releasedWaterInMillilitres / 1000




# 1 Megalitre of water is equal = 1 000 000 litres
megaInLitres = 1000000

amaoutOfWaterLeft = megaInLitres - releasedWaterInLitres
waterInPercentage = 930000 / 1000000 * 100
print("Amount of water released", releasedWaterInLitres)
print("Amount of water left", amaoutOfWaterLeft)
print(waterInPercentage)
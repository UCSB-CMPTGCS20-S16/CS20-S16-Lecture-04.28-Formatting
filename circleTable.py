

from circleFunctions import areaCircle
from circleFunctions import circumferenceCircle

def circleTable(startRadius,stopRadius):
    print "%10s %10s %15s" % ("radius", "area", "circumference")
    
    for radius in range(startRadius,stopRadius):
        print "%10.5f %10.5f %15.5f" % (radius,areaCircle(radius),circumferenceCircle(radius))


if __name__ == "__main__":
  circleTable(10,20)


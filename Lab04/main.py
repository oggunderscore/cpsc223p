# Begin testing here

# Testing Basics

from mathematics import whoami as normalWhoAmI

mName = normalWhoAmI.getName()

print (f'Base Name: {mName}\n')

# Testing Numbers

from mathematics.numbers import whoami as numbersWhoAmI
from mathematics.numbers import series

numbersName = numbersWhoAmI.getName()
numbersSum = series.sum_values(nums = [1,2,3,4,5]) # Assert 15
numbersAvg = series.average_values(nums = [3,5,7]) # Assert 5

print(f'Numbers Name: {numbersName}\nSum: {numbersSum}\nAverage: {numbersAvg}\n')

from mathematics.numbers.simple import addition, subtraction, multiplication, division # Explicit import

x = 15
y = 5

print (f'15+5 = {addition(x=x, y=y)}\n15-5 = {subtraction(x=x, y=y)}\n15*5 = {multiplication(x=x, y=y)}\n15/5 = {division(x=x, y=y)}\n')

# Testing Geometry

from mathematics.geometry import whoami as geoWhoAmI
from mathematics.geometry import circle, cube

geoName = geoWhoAmI.getName()

print(f'Geometry Name: {geoName}\nCircle with Radius 3:\nCircumference = {circle.circumference(3)}\nArea = {circle.area(3)}\n')
print(f'Cube with side length 5:\nSurface Area = {cube.surface_area(side=5)}\nVolume = {cube.volume(side=5)}\n')

from mathematics.geometry.rectangle import perimeter, area # Explicit import

print(f'Rectangle that is 5L x 3W:\nPerimeter = {perimeter(length=5, width=3)}\nArea = {area(length=5, width=3)}')
# Begin testing here

from mathematics import whoami as normalWhoAmI

mName = normalWhoAmI.getName()

print (f'Base Name: {mName}\n')

# Testing Module Numbers

from mathematics.numbers import whoami as numbersWhoAmI
from mathematics.numbers import series

numbersName = numbersWhoAmI.getName()
numbersSum = series.sum_values(1,2,3,4,5) # Assert 15
numbersAvg = series.average_values(3,5,7) # Assert 5

print(f'Numbers Name: {numbersName}\nSum: {numbersSum}\nAverage: {numbersAvg}\n')

from mathematics.numbers.simple import addition, subtraction, multiplication, division

x = 15
y = 5

print (f'15+5 = {addition(x, y)}\n15-5 = {subtraction(15, 5)}\n15*5 = {multiplication(x, y)}\n15/5 = {division(x, y)}\n')


import math

print("\nHowdy, welcome to the interactive calculator by Daniel Nishiyama.") #Welcome prompt to familiarize user w/ program
print("When entering a number for the user prompt, please don't use commas in your numbers and enter numbers to two decimal places only.")
print("Numbers like 107849, or 1.58 are acceptable.\n") #prompt as user guide

print("Finding the radius of a circle in inches:") #whichever the program is looking for
print("Formula for finding the radius of a cricle is: radius = sqrt(Area/pi)") #shows user equation for finding x
print("Please enter number in inches:")
area = float(input()) #user input in float
radius_formula = math.sqrt(area/math.pi) #formula to solve for x
print("Radius is: {:.3f}in".format(radius_formula), '\n') #outputs x and uses {.3f} to round, also uses .format for cleaner output

print("Findng the side length of an equilateral triangle:")
print("Formula for finding the side length of an equilateral triangle is: a = (2/3)3^(3/4) * sqrt(Area)")
print("Please enter number in inches:")
area = float(input())
triang_formula = (2/3) * (pow(3, 3/4) * math.sqrt(area))
print("Side length is: {:.3f}in".format(triang_formula), '\n')

print("Finding the side length of a square:")
print("Formula for finding the side length of a square is: a = sqrt(Area)")
print("Please enter number in inches:")
area = float(input())
square_formula = math.sqrt(area)
print("Side length is: {:.3f}in".format(square_formula), '\n')

print("Finding the side length of a regular pentagon:")
print("Formula for finding the side length of a regular pentagon is: sqrt(Area/((1/4) * sqrt(5 * (5 + 2 * sqrt(5))))))")
print("Please enter number in inches:")
area = float(input())
pentagon_formula = math.sqrt(area/((1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5)))))
#pentagon_formula =
print("Side length is: {:.3f}in".format(pentagon_formula), '\n')

print("Finding the side length of a regular dodecagon(12 sides):")
print("Formula for finding the side length of a regular dodecagon is: sqrt(area/3 * (2 + sqrt(3)))))")
print("Please enter number in inches:")
area = float(input())
dodecagon_formula = math.sqrt(area/(3 * (2 + math.sqrt(3))))
print("The side length is: {:.3f}in".format(dodecagon_formula), '\n')
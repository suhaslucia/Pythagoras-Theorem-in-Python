from math import sqrt #importing math package

print(" ----------Pythagoras Theorem to Find the sides of the Triangle---------- ")
print(" ------------ Enter any one side as 0 to obtain the result -------------- ")

# Taking the inputs as a integer value from the user
base = int(input("Enter the base of the Triangle: "))
perpendicular = int(input("Enter the perpendicular of the Triangle: "))
hypotenuse = int(input("Enter the hypotenuse of the Triangle: "))

# Calculating the Hypotenuse value and printing it
if hypotenuse == 0:
    b = base ** 2
    p = perpendicular ** 2
    hyp = b + p
    result = sqrt(hyp)
    print(f'\n Hypotenuse of Triangle is {result}')
    
# Calculating the Perpendicular value and printing it
elif perpendicular == 0:
    b = base ** 2
    hyp = hypotenuse ** 2
    p = hyp - b
    result = sqrt(p)
    print(f'\n Perpendicular of Triangle is {result}')
    
# Calculating the Base value and printing it
else:
    p = perpendicular ** 2
    hyp = hypotenuse ** 2
    b = hyp - p
    result = sqrt(b)
    print(f'\n Base of Triangle is {result}')

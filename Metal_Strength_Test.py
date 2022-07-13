print("Howdy, welcome to this program which will determine the strain type and stress # given the strain number.")

print("\nInterval O to A is: (0,0),(O.01,43)")
print("Interval A to B is: (0.01,43),(0.03,44)")
print("Interval B to C is: (0.03,44),(0.06,45)")
print("Interval C to D is: (0.06,45),(0.17,60)")
print("Interval D to E is: (0.17,60),(0.27,53)\n") #tells user where strain is on graph

print("When inputting a #, please do not put negatives and anything greater than 0.27.")
x_val = float(input("Enter a strain #:"))
strain_type = ""
stress_num = 0

if x_val < 0: #checks if user input is less than 0
    print("Error, please enter a # greater than 0.")
    exit() #stops running program after error

if x_val > 0.27:#checks if user input is greater than max input
    print("Steel has broken.")
    exit()

if 0 < x_val <= 0.01: #determines strain type using if statements
    strain_type = "linear"
elif 0.01 <= x_val <= 0.06:
    strain_type = "plastic"
elif 0.06 <= x_val <= 0.17:
    strain_type = "strain hardening"
elif 0.17 <= x_val <= 0.27:
    strain_type = "necking"

y_val = 0 #find slope using endpoints of interval

if 0 < x_val <= 0.01: #determines stress # using if statements
    y_val = ((43-0)/(0.01)) * (x_val - 0.01) + 43 #use two point form formula to solve for y_val
elif 0.01 <= x_val <= 0.03:
    y_val = ((44-43)/(0.03-0.01)) * (x_val - 0.01) + 44
elif 0.03 <= x_val <= 0.06:
    y_val = ((45-44)/(0.06-0.03)) * (x_val - 0.03) + 45
elif 0.06 <= x_val <= 0.17:
    y_val = ((60-45)/(0.17-0.06)) * (x_val - 0.06) + 60
elif 0.17 <= x_val <= 0.27:
    y_val = ((53-60)/(0.27-0.17)) * (x_val - 0.17) + 53

print("Point on Stress-strain graph is: ({},{})".format(x_val,y_val)) #prints point where user input would be
print("Steel strain # is", x_val, "and strain type is", strain_type) #prints strain # and strain type
print("Stress # of steel is", y_val) #prints users stress # aka y value
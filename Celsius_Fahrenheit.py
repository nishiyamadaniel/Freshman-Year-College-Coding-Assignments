celsius = 0
fahrenheit_list = []
list = []

#opens and read dat file
celsius_data = open('Celsius.dat')

#adds each row or line to list
for line in celsius_data:
    list.append(line)

#removes extraneous characters in list
list = [x.replace("''", "").replace("\n","") for x in list]

#converts list to a float
for x in range (0, len(list)):
    list[x] = float(list[x])

#calculates celsius to fahrenheit and appends to fahrenheit list
for x in range(0, len(list)):
    cToF_equation = ((9 / 5) * list[x] + 32)
    fahrenheit_list.append(cToF_equation)

#opens fahrenheit dat file
with open('Fahrenheit.dat', 'a') as f:
#traverses through length of list which is same length as fahrenheit list to output fahrenheits list data
    for x in range(0, len(list)):
        f.write("{} F\n".format(fahrenheit_list[x]))

# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, nor tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Daniel Nishiyama
# Section: 533
# Assignment:Individual Lab 9 Activity 3
# Date:28 October 2021

import csv
from statistics import stdev

#assign min_temp to arbitrarily large # for progam to work
min_temp = 1000
max_temp = 0
precipitation_list = []
avg_precipitation = 0
day_count = 0
humidity_90 = 0
avg_highTemp_july = 0

#opens csv file
with open('WeatherDataWindows.csv') as f:
#adds rows to a list
    reader = csv.reader(f, delimiter = ',')
#skips first row
    next(reader)
    for data in reader:
        day_count += 1

#takes column data and adds to variable
        minimum_temp = float(data[3])
        maximum_temp = float(data[1])
        precipitation = float(data[-1])
        precipitation_list.append(precipitation)
        humidity_high = float(data[7])

#takes month, date and year and assigns to variables for later use
        month, date,year = data[0].split('/')
        month, date,year = int(month), int(date), int(year)

#checks for max temp in month and year
        if month == 7 and year == 2015:
            avg_highTemp_july += maximum_temp

#if humidity is higher than 90, increase humidity by 1
        if humidity_high > 90:
            humidity_90 += 1

#compares max and min temperature and reassigns to variable
        if max_temp < maximum_temp:
            max_temp = maximum_temp
        if min_temp > minimum_temp:
            min_temp = minimum_temp

#gets each # from precipitation list and adds to avg_precipitation to solve for average later
    for x in precipitation_list:
        avg_precipitation += precipitation_list[int(x)]
        x += 1

#equations to solve for certain variables
    avg_precipitation = round(avg_precipitation/len(precipitation_list), 3)
    humidity_eq = round((humidity_90 / day_count) * 100, 3)
    avg_highTemp_july = round((avg_highTemp_july / 31), 3)

#prints needed info out
print("\nMaximum Temperature:", max_temp, 'F')
print("Minimum Temperature:", min_temp, 'F')
print("Average Daily Precipitation:", avg_precipitation,'in')
print("Average high temperature for July 2015:", str(avg_highTemp_july), 'F')
print("Percentage of days when humidity was above 90%:", str(humidity_eq) + '%')
print("Mean for precipitation levels is:", avg_precipitation, 'in')
print("Standard deviation for precipitation levels is:", round(stdev(precipitation_list), 3))



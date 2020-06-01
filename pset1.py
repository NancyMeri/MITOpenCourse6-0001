#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:59:39 2020

@author: nancy
"""

# part A- House Hunting
annual_salary = float (input("Enter your annual salary: "))
portion_saved = float (input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float (input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
months = 0

while (current_savings < total_cost*portion_down_payment):
    current_savings += current_savings*r/12 #monthly return on investment
    current_savings += (annual_salary/12)*portion_saved
    months += 1
print("Number of months: " + str(months))

# part B- Saving, with a Raise
annual_salary = float (input("Enter your starting annual salary: "))
portion_saved = float (input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float (input("Enter the cost of your dream home: "))
semi_annual_raise = float (input("Enter the semi-­annual raise, as a decimal: "))
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
months = 0 #number of months

while (current_savings < total_cost*portion_down_payment):
    current_savings += current_savings*r/12 #monthly return on investment
    current_savings += (annual_salary/12)*portion_saved
    months += 1
    if ((months-1)%6 == 0 and months > 6): #need and b/c otherwise it counts the first month
        annual_salary += (annual_salary*semi_annual_raise)
print("Number of months: " + str(months))
#print (str(current_savings)) <-- use this to test if you're > down payment

# part C- Finding the right amount to save away
starting_annual_salary = float (input("Enter the starting salary: "))
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
semi_annual_raise = 0.07
current_savings = 0.0
portion_saved = 1
months = 0
annual_salary = starting_annual_salary
while (current_savings < total_cost*portion_down_payment):
    current_savings += current_savings*r/12 #monthly return on investment
    current_savings += (annual_salary/12)*portion_saved
    months += 1
    if ((months-1)%6 == 0 and months > 6): #need and b/c otherwise it counts the first month
        annual_salary += (annual_salary*semi_annual_raise)
if (months > 36):
    print ("It is not possible to pay the down payment in three years.")
else:
    steps = 0
    low = 0
    high = 10000
    epsilon = 100 #acceptable range of error
    guess = (high + low)//2
    while abs(current_savings - (portion_down_payment*total_cost)) >= epsilon:
        steps += 1
        months = 0
        current_savings = 0.0
        annual_salary = starting_annual_salary
        portion_saved = guess / 10000
        while (months < 36):
            current_savings += current_savings*r/12 #monthly return on investment
            current_savings += (annual_salary/12)*portion_saved
            months += 1
            if ((months-1)%6 == 0 and months > 6): #need and b/c otherwise it counts the first month
                annual_salary += (annual_salary*semi_annual_raise)
        if current_savings < (portion_down_payment*total_cost):
            low = guess
        else:
            high = guess
        guess = (high + low)//2
    print ("Best savings rate: " + str(guess/10000.0))
    print ("Steps in bisection search: " + str(steps))
    # print ("Total savings this way: " + str(current_savings)) <-- use this to test if you're close enough

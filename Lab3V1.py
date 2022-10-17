# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:54:00 2022

@author: Aloy
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:42:28 2022

@author: Aloy
"""
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name:
# Student CCID:
# Others:
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions may be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import matplotlib.pyplot as plt
import numpy as np
import math as math

print('Version 1 - Solution')
months = 0
balance= 2000
interestrate= 6.25/1200
year = 0
year = 0
increaserate= 7/100
artcost= 5550
sciencecost= 6150
engineeringcost= 6550

savings = [] #I added this variable to hold the new monthly savings
for month in range(0,215):
    month = month + 1
    year = year + 1/12
    interest= (interestrate) * (balance)
    balance = (balance + interest + 200)
    
    balance2 = [balance]
    counter = [balance2]
    savings.append(round(balance, 2))
    for year in range (0,18):
           #It added the new value to the saving variable
          counter = [balance2]
print(savings)
print("The Total savings amount is $%.2f"%balance)
for year in range(0,21):
    year= year + 1
    artincrease= artcost*increaserate
    scienceincrease= sciencecost*increaserate
    engineeringincrease= engineeringcost*increaserate
    artcost= artcost+artincrease
    sciencecost= sciencecost+scienceincrease
    engineeringcost= engineeringcost+engineeringincrease
    if year== 18:
      artcost_19= artcost
      sciencecost_19=sciencecost
      engineeringcost_19=engineeringcost
    if year== 19:
      artcost_20= (artcost)
      sciencecost_20=sciencecost
      engineeringcost_20=engineeringcost
    if year== 20:
      artcost_21= (artcost)
      sciencecost_21=sciencecost
      engineeringcost_21=engineeringcost
    if year== 21:
      artcost_22= (artcost)
      sciencecost_22=sciencecost
      engineeringcost_22=engineeringcost
totalartcost= artcost_19+artcost_20+artcost_21+artcost_22
totalsciencecost =sciencecost_19+sciencecost_20+sciencecost_21+sciencecost_22
totalengineeringcost= engineeringcost_19+engineeringcost_20+engineeringcost_21+engineeringcost_22
print("The cost of the arts program is $%.2f" %totalartcost)
print("The cost of the science program is $%.2f" %totalsciencecost)
print("The cost of the engineering program is $%.2f" %totalengineeringcost)
# ------------Remove any code that is unnecessary--------------------------
counter = [balance2]
art= [totalartcost]
science = [totalsciencecost]
engineering = [totalengineeringcost]
for year in range(0,17):
    counter += [balance2]
    art += [totalartcost]
    science += [totalsciencecost]
    engineering += [totalengineeringcost]
y=savings
years = range(0,215)
#y=balance2
plt.plot( years,y,label = 'Savings Balance')
plt.ylabel ('Amount $')
plt.xlabel ('Month')
plt.title ('Savings vs Tuition')
plt.show()

    
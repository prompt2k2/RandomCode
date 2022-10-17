import numpy_financial as npf
import numpy as np

# compound interest rate

deposit = 2000
annual_rate = 0.0625
monthly_rate = annual_rate/12
contribution = 200
year = 18

total_savings = []

for year in range(0, 18):

    new_deposit = round(deposit + (deposit * monthly_rate) + contribution, 2)
    total_savings.append(new_deposit)
    deposit = new_deposit
    
print(total_savings)
print("The Total savings amount is ", sum(total_savings))

#Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food and then calculate the amounts 
# with an 18 percent tip and 7 percent sales tax. Display each of
# these amounts and the total price.

#Using array total and calculating tip, tax, and total then assigning each to an index in total
#then print array total.

import array as arr
#initialize a float array to store meal cost, tip, tax and total
total = arr.array('d', [])

print("Hello, I hope the meal was good!")

total.append(float(input('Enter the amount for the meal: ')))#input total for meal at index 0 of total array
total.append((total[0] * 0.18)) #append tip into index 1
total.append((total[0] * 0.07)) #append tax into index 2
total.append((total[0] + total[1] + total[2])) #append total + tip + tax 

print('The cost of the meal was: $', "%.2f" % total[0])
print('The 18% tip is: $', "%.2f" % total[1])
print('7% Sales Taxes is: $', "%.2f" % total[2])
print("Total for meal is: $", "%.2f" % total[3])
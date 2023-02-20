'''
#Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 
# For example factorial of 5 is 5*4*3*2*1 which is 120. 
# Use what you learned about while loop to create a program that calculates the factorial value of of a positive integer. 
# Your program should ask a user to enter a number equal or greater than 0 , it calculates the value of its factorial and print it. 

'''

num = int(input("Please enter a integer that is not negative: ")) 
  
factorial = 1
  
while num > 0: 
    factorial = factorial * num 
    num -= 1 
  
print("The Factorial of the number you have given is :" ,factorial)
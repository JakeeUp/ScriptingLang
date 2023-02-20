
'''
Using while loop write a Python Program that calculates and prints the sum of integer numbers (1+2+3+4+......+n) 
where n is a number determined by the user.

'''

n = int(input("Please enter a number: "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum of the numbers from 1 to", n, "is", sum)


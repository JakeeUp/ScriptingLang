'''
define The prices of items in a shopping cart are represented by the following list [10,20,30,45, 32]. 
Use a for loop to calculate and print the total price of the items in the shopping cart.
'''

total_price = 0
for item in [10,20,30,45,32]:
    total_price += item
print(total_price)
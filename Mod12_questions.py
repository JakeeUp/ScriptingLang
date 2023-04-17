# import Mod1_user as Userr

# user2 = Userr.User("John", "Doe")
# user2.describe_user()

# from Mod1_user import User

# user1 = User("Jane", "Doe","Email","Addy")
# user1.describe_user()

# import math

# MyList = [1, 2, 3, 4, 5, 6, 7]

# for item in MyList:
#     sqrt_val = math.sqrt(item)
#     print("Square root of", item, "is", sqrt_val)


numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

min_num = min(numbers)
max_num = max(numbers)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")




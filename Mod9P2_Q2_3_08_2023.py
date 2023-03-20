#Assume that the variable data refers to the dictionary {'b':20, 'a':35} .Write the expressions that perform the following tasks:Print the keys in data in alphabetical order..

data = {'b':20,'a':35}


sorted_data = sorted(data.keys());print(sorted_data)


print(data)


'''

1. data['b'] = -data['b']
2. data.update({"c":40}) or data['c']=40
3. data.pop('b')
4. sorted_data = sorted(data.keys());print(sorted_data)


'''

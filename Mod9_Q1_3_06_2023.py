
# Colors being defined
colors =  ('blue', 'red', 'green', 'orange', 'pink', 'purple', 'red')

# Prints the length of colors tuple
print(len(colors))

# Prints the second and third item of the tuple 
print(colors[1], colors[2])

# Use negative indexes to print 'orange' and 'pink'
print(colors[-4], colors[-2])

# Check if 'red' in colors tuple
print('red' in colors)

# Check for the first occurrence of 'red'
print(colors.index('red'))

# Create another tuple called data with the following items inside: 1, 2, 3, 4, 5
data = (1, 2, 3, 4, 5)

# Join the two tuples in a new tuple called colorsdata
colorsdata = colors + data
print(colorsdata)

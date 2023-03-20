dictionary = {'d': -120, 'b':-20, 'a':35, 'c': 15}

if len(dictionary) == 0:
  print("None")
else:
  largest_value = max(dictionary.values())
  print(largest_value)



dictionary = {'d': -120, 'b':-20, 'a':35, 'c': 15}

if len(dictionary) == 0:
    print(None)
else: 
    largest_value = -float('inf')

    for key in dictionary:
        if dictionary[key] > largest_value:
            largest_value = dictionary[key]

    print(largest_value)

dictionary = {'d': -120, 'b':-20, 'a':35, 'c': 15}
if not dictionary:
  print(None)
else:
  min_val = min(dictionary.values())
  print(min_val)


  
dictionary = {'d': -120, 'b':-20, 'a':35, 'c': 15}

if len(dictionary) == 0:  
    print("None")
else:  
    min_value = float('inf') 

    for key in dictionary:  
        if dictionary[key] < min_value:  
            min_value = dictionary[key]  

    print(min_value)


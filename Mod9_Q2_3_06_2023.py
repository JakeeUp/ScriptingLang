SetB = {'Lexus','Ford','Audi'}
SetB.add('Honda')
print(SetB)

SetA = {'Ford','Toyota','Dodge','Nissan'}
SetA.discard('Nissan')
print(SetA)

SetC = SetA|SetB
print(SetC)

common_items = SetA & SetB
print(common_items)

difference_items = SetA - SetB
print(difference_items)

sym_dif_items = SetA ^ SetB
print(sym_dif_items)

print(SetA.intersection(SetB))
print(SetA.symmetric_difference(SetB))
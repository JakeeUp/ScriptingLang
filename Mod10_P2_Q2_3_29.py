def calc_area(length, width):
    area = length * width
    return area

def calc_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calc_area(length, width)
perimeter = calc_perimeter(length, width)

print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)


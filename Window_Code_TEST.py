#testing of a window output in python
import tkinter

window = tkinter.Tk()
window.title("Shopping Cart")
window.geometry("400x200")
 
output_label = tkinter.Label(window, text="Shopping Cart Output code") 
output_label.pack() 
  
#making a class like in unity
class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def calculateTotalPrice(self):
        totalPrice = 0
        for item in self.items:
            totalPrice += item
        return totalPrice

cart = ShoppingCart([10, 20, 30, 45, 32]) 
totalPrice = ("the total price of the shopping cart is: ",cart.calculateTotalPrice())
code_output= totalPrice

output_label = tkinter.Label(window, text=code_output) 
output_label.pack() 

window.mainloop()
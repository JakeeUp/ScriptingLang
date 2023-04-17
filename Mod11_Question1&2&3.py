class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("Pizza House", "Italian")
print(f"Number of customers served: {restaurant.number_served}")
restaurant.number_served = 50
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(25)
print(f"Number of customers served: {restaurant.number_served}")

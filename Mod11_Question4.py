

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User Information: \n\tName: {self.first_name} {self.last_name}\n\tAge: {self.age}\n\tEmail: {self.email}\n\tLocation: {self.location}\n")
    
    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome back.\n")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('John', 'Doe', 'johndoe@gmail.com', 'New York',10)
user2 = User('Jane', 'Doe', 'janedoe@gmail.com', 'San Francisco',20)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3 = User('Jacob', 'doe', 30, 'jacobdoe@gmail.com', 'Texas')

user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()

print(f"Login attempts: {user3.login_attempts}")

user3.reset_login_attempts()

print(f"Login attempts after reset: {user3.login_attempts}")

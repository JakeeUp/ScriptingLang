class User:
    def __init__(self, first_name, last_name, email, address):
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.address = address

    def describe_user(self):
        print('\nuser full name ' +self.first_name+ ' '+ self.last_name)
        print('email= ', self.email)
        print('address= ', self.address)
    
    def user_greeting(self):
        print('Hello '+ self.first_name+' '+ self.last_name)
    
user1= User ('Meerna', 'Ammari', 'meerna.ammari@company.com', '159 Jasmin Spur')
user2= User ('Kevin', 'Ammari', 'Kevin.ammari@company.com', '159 Jasmin Spur')
user3= User ('Nada', 'Masri', 'Nada.Masri@company.com', '3308 Honey flower ct.')

# user1.describe_user()
# user1.user_greeting()

# user2.describe_user()
# user2.user_greeting()

# user3.describe_user()
# user3.user_greeting()


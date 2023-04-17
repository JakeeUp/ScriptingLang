class Student:
    def __init__(self, first_name, last_name, email, hours_completed, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hours_completed = hours_completed
        self.gpa = gpa

    def determine_grade_level(self):
        if self.hours_completed <= 30:
            return "Freshman"
        elif self.hours_completed <= 60:
            return "Sophomore"
        elif self.hours_completed <= 90:
            return "Junior"
        else:
            return "Senior"

    def scholarship_gpa_check(self):
        if self.gpa > 2.5:
            print(f"{self.first_name} {self.last_name} is eligible for scholarship application")
    
    def greet_high_gpa(self):
        if self.gpa >= 3.5:
            for i in range(4):
                print(f"Hi {self.first_name} {self.last_name}!")
        else:
            print(f"Hi {self.first_name} {self.last_name}!")


student1 = Student("John", "Doe", "johndoe@email.com", 115, 3.8)
student2 = Student("Jane", "Smith", "janesmith@email.com", 15, 2.3)


print(student1.determine_grade_level()) 
print(student2.determine_grade_level())  

student1.scholarship_gpa_check()  
student1.greet_high_gpa() 
student2.scholarship_gpa_check()  
student2.greet_high_gpa()  

#one plus two
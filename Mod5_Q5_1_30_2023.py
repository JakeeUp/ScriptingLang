#User Inputs for hw,rh, and ot
hourly_wage = float(input("Enter hourly wage: ")) 
regular_hours = float(input("Enter total regular hours: ")) 
overtime_hours = float(input("Enter total overtime hours: ")) 

#Calculating the total weekly pay
total_weekly_pay = (hourly_wage * regular_hours) + (1.5 * hourly_wage * overtime_hours) 

#Printing the total weekly pay
print("Total weekly pay is $%.2f" %total_weekly_pay)
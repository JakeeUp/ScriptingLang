hours = float(input("Umm, how many hours did ya work this week? "))
pay = float(input("Alrighty, so how much do ya make per hour? "))

if hours > 35:
  overtime_hours = hours - 35
  overtime_pay = pay * 1.75
  total_pay = (35 * pay) + (overtime_hours * overtime_pay)
  print("Wowee! You worked some overtime, so you'll be makin'", total_pay, "bucks!")
else:
  total_pay = hours * pay
  print("Looks like you didn't work no overtime, so you'll be takin' home", total_pay, "bucks.")

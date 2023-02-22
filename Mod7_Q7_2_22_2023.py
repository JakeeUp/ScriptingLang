#extra assignment

first_num = int(input("Enter lower range: ")) 
second_num = int(input("Enter upper range: ")) 
  
print("Prime numbers between",first_num,"and",second_num,"are:") 
  
for num in range(first_num,second_num + 1):  
   if num > 1: 
       for i in range(2,num): 
           if (num % i) == 0: 
               break 
       else: 
           print(num)
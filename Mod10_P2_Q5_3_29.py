def calc_total(num_old, num_new):
    cost_old = num_old * 2.00
    cost_new = num_new * 3.00
    total_cost = cost_old + cost_new
    return total_cost

num_old = int(input("Enter the number of old DVDs you want to rent: "))
num_new = int(input("Enter the number of new DVDs you want to rent: "))
total_cost = calc_total(num_old, num_new)

print("Total cost of rental: $", total_cost)
#make a system that uses a for loop to where you tip and you get 3 different options of tipping and depending on what you tip theres different print prompts that come up
tip_choice = int(input("\nWhat would you like to tip? \n1. 5 percent \n2. 10 percent \n3. 100 percent\n"))
if tip_choice == 1:
    tip = total_cost * 0.05
    print("\nDefualt Ending:\nthanks for the", tip_choice * 5, "percent tip! of $", tip , "im sure i can get soooooo much with that") 
elif tip_choice == 2:
    tip = total_cost * 0.10
    print("\nDefault Ending:\nThank you for the", tip_choice * 5, "percent tip! of $", tip) 
elif tip_choice == 3:
    tip = total_cost 
    print("\nI HAVE NEVER GOTTEN THIS BIG OF A TIP IN MY LIFE THANK YOU SO MUCH TAKE A FREE DVD")
    movie_choice = int(input("\n what movie would you like to take? \n1. Scary movie \n2.Final Destination \n3.Saw \n4. These selections suck\n"))
    if movie_choice == 1:
        print("\nDefualt Ending:\nYour a scary movie type? i assumed so")
    elif movie_choice == 2:
        print("\nDefualt Ending:\nThe wrap around of that franchise is kinda heat")
    elif movie_choice == 3:
        print("\nDefualt Ending:\nGet outta here")
    elif movie_choice == 4:
        print("\nYou tryna go outside and box right now? I gave you a free movie")
        fighting_choice = int(input("\ndo you want to go outside and fight the dvd manager? \n1.yes \n2.no\n"))
        if fighting_choice == 1:
            print("\nSpecial Ending 1:\nyou went outside and got your butt handed to you")
        if fighting_choice == 2:
            print("\nSpecial Ending 2:\nyou were the bigger person and left the area")
else:
    tip = 0
    print("\nInhumane Ending:\ni cant even get a penny? get outta here.")

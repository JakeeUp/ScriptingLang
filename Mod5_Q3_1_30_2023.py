#Five Star Retro Video Rental Program
new_videos = int(input("How many new movies are we renting today? "))
old_videos = int(input("How many old moves are we renting today? "))

#Calculating the total cost of rent for new and old videos
total_cost = (new_videos * 3) + (old_videos * 2) 

#Printing output total cost to user 
print("Okay man, your total cost will be $" + str(total_cost) + " will this be cash or card?")
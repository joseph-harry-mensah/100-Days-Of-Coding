#This program collects names of friends separated by a comma and a space
#It then splits the names in a list and picks randomly a friend who will pay for lunch/ meal


import random



names = input("Enter the names of all your friends. Eg: John, Michal\n")

new_names = names.split(",") #This  .split(",") creates a list from the names


#total numer of items in list
num_items = len(new_names)


#using the total number of items to randomise a number 
#prints a name from the list (newnew_names) using index

#  random_num = random.randint(0, num_items - 1)
#  print(f'{new_names[random_num]} is going to pay for the meals today')


# We can equally simply use random.choice to solve the same problem with little code

print(random.choice(new_names)+ " will pay for today's meals")
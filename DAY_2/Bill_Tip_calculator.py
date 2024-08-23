# Tip and Bill calculator

print("Welcome to Tip Calculator, " + input("What is your name"))


# I did conversion of the inputs to a float dtype
total_bill = float(input("What was the total bill?"))
#new_total_bill = float(total_bill)

n_people = int(input("How many people to split the bill?"))
#new_n_people = float(n_people)


tip_percent = float(input("How much tip (percentage) would you like to give: 10, 12 or 15?"))
#new_tip_percent = float(tip_percent)


# I used this analogy: Total bill + chosen percentage of the bill and divided by the number of people paying together
#bill_split = ((total_bill + ((tip_percent/100)* total_bill)) / n_people)
bill_split= round(((total_bill + ((tip_percent/100)* total_bill)) / n_people),2)

#Rounded bill_split to 2 decimal places and onverted it to a string dtype before printing
#print(" Every person will pay $" + str(round(bill_split, 2)))


#Better approach using format (F-string) 
message = f"Each person should pay: ${bill_split}"
print(message)

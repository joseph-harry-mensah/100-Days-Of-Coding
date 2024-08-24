#Rollercoaster Game
#You need to be 120cm in height or better to use the  service
#$5 for users <12 yrs, $7 for users <=18yrs, $12 for users > 18yrs
#If want to take Photos, you additional $3 dollars to the total bill


print("Welcome to the Rollercoaster Ride Station")
height = int(input("What is your height?"))


    #Using nested if-elif-else statements for the user validation and ticket prices 
if height >=120:
    print("Great!! You can ride on the Rollercoaster")
   
  
    age = int(input("What is your age?"))
    
    if age <12:
        bill = 5
        print("Child tickets $5")
        
    elif age <=18:
        bill = 7
        print("Youth tickets are $7")
        
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay. Enjoy your ride")
    
    else:
        bill = 12
        print("Adult tickets are $12")
        
        
            
            
    want_photo = input("Do you want a photo taken? (Yes or No)")
    photo = 3   # $3

    
    
     #Adding option to opt for photos, price will be added to the total bill
        # A photo taken costs $3
    if want_photo =="Yes" or want_photo =="YES" or want_photo =="yes":
        
        
        # += photo adds $3 to the bill 
        if age < 12:
            bill += photo
            message = f"The total bill is ${bill}"
            print(message)
        
        elif age <= 18:
            bill += photo
            message = f"The total bill is ${bill}"
            print(message)
            
        elif age >= 45 and age <= 55:
            print("You recieve a free photo as well")
        
        else:
            bill += photo
            message = f"The total bill is ${bill}"
            print(message)
            
            
        
    else: 
        if age < 12:
            message = f"The total bill is ${bill}"
            print(message)
        
        elif age<=18:
            message = f"The total bill is ${bill}"
            print(message)
            
        elif age >= 45 and age <= 55:
            print("No photo requested")
        
        else:
            message = f"The total bill is ${bill}"
            print(message)
            
            
            
else:
    print("Sorry, grow taller and try next time. We look forward to seeing you soon")

    

        
    
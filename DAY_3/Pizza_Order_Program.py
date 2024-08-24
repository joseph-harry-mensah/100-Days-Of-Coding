#This program asks the user the which size of pizza they want
#Ask if they want pepperoni or extra cheese
#Based on their input, we determine their final bill



size = input("Welcome to McHarry's Pizza Place.\n What size of pizza do you want (Small | Medium | Large)")


if size == "small" or size == "Small" or size == "SMALL":
    bill = 15
    print("Small-size Pizza is $15")

    
elif size == "medium" or size =="Medium" or size =="MEDIUM":
    bill = 20
    print("Medium-size Pizza is $20")
    
    
else:
    bill = 25
    print("Large-size Pizza is $25")

    
    
    
 # Additional things they can order for the pizza

extra_cheese = 1    
pepperoni_ssize = 2
pepperoni_other_size = 3  



want_pepperoni = input("Do you want pepperoni? ( Yes | No)")


if want_pepperoni == "Yes" or want_pepperoni == "YES" or want_pepperoni =="yes":
    
    if size =="small":
            bill += pepperoni_ssize
            
    else:
            bill += pepperoni_other_size
                   
else:
    bill = bill
    
        
    
    
add_cheese = input("Do you want extra cheese")
if add_cheese == "yes" or add_cheese  =="Yes" or add_cheese =="YES":
        bill += extra_cheese
        message = f"Final Bill is : ${bill}"
        print(message)
                
                
else:
        message = f"Final Bill is : ${bill}"
        print(message)
                
        
        
        
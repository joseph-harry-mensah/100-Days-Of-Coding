#Fizz Buzz Game
#Prints numbers from 1 - 100
# Prints "Fizz" when number is divisible by 3
# Prints "Buzz" when number is divisible by 5
# Prints "FizzBuzz" when number is divisible by 3 and 5




# Creating a range of numbers between 0 and 101
for number in range(1, 101, 1):
    
    # conditions
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        
    elif number % 3 == 0:
        print("Fizz")
        
    elif number % 5 == 0:
        print("Buzz")
        
        
       #print the results 
    else:
        print(number)
        
        
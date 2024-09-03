#This program checks if a number is a prime number


number = int(input("Check if number is prime: "))



def check_prime(num):
    
    is_prime = True
    
    for i in range(2, number): 
        if number % i == 0:
            is_prime = False
            
            
    if is_prime:
        print(f"{num} is a prime number")
    
    
    
    else:
        print(f"{num} is not a prime number")
            
            
                                               
                  
check_prime(num = number)

# This is a Cipher program using Caesar Cipher
#User can choose between encrypting and decrypting a message


# This is for encryption and decryprion Helps resolve issue of last alphabet 'z' not causing a bug
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



    
 # Implementing Caesar Decryption    
def caesar(user_text, shift_amount, cipher_choice):
    end_text = ""
    
    if cipher_choice =="decode":
            shift_amount *= -1
    
    
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
            
        else:
            end_text += char
    print(f"The {choice}d text is {end_text}")
            


# Program loop
should_continue = True

while should_continue:
        
#Taking input
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt \n").lower()
    text = input("Type your message:\n").lower()
    shift_num = int(input("Type the shift number\n"))
    
    shift_num = shift_num % 26        #shift  number of letters down to fit the alphaet variable

    caesar(user_text = text, shift_amount= shift_num, cipher_choice=choice)




# Looping the program
    program_status = input("Type 'yes' if you want to go again. Otherwise,type 'no' to end program").lower()

    if program_status =="no":
        should_continue = False
        print("Program has ended, Good Bye User")

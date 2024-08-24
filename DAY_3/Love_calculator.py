#Love calculator program the names of both couples as input
#Checks the number of times the letters in the word TRUE occurs
#Then checks the number for number of times the letters in the word LOVE occurs.
#Then combine these numbers to make a 2 digit number




print("Welcome to Love Calculator! \n We test compatibility between couples using tried-and-tested Scientific Method by BuzzFeed")

name1 = input("What is your name\n")
name2 = input("What is the name of your partner\n")



#Need to change the names to lower case before counting to ensure accuracy

combined_names = name1 + name2
lowercase_names = combined_names.lower()

t = lowercase_names.count("t")
r = lowercase_names.count("r")
u = lowercase_names.count("u")
e = lowercase_names.count("e")


l = lowercase_names.count("l")
o = lowercase_names.count("o")
v = lowercase_names.count("v")
e = lowercase_names.count("e")



total_lowercase_count = t + r + u + e
total_love_count = l + o + v + e
message1 = f"T occurs {t} times \n R occurs {r} times \n U occurs {u} times \n E occurs {e} times"
message2 = f"L occurs {l} times \n O occurs {o} times \n V occurs {v} times \n E occurs {e} times"
total1 = f"Total =  {total_lowercase_count}"
total2 = f"Total =  {total_love_count}"



#printing LOVE atotal_lowercase_count, same for TRUE
print(message1)
print(total1)

print(message2)
print(total2)


#concatinating the total of TRUE and LOVE as str dtype and print it
truelove_score = str(total_lowercase_count) + str(total_love_count)
truelove_score = int(truelove_score)



#condition and conclusion

if truelove_score < 10 or truelove_score >90:
    prompt1 = f"Your score is {love_score}, and you go together like coke and mentos"
    print(prompt1)
    
elif truelove_score >40 and truelove_score <50:
    prompt2 = f"Your score is {love_score}, you are alright together"
    print(prompt2)
    
else:
    prompt3 = f"Your score is {love_score}"
    print(prompt3)

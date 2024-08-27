#Compares scores of students and display the highest score



student_scores = input("Enter the numbers here. Eg: 20 4 1\n").split()

for score in range(0, len(student_scores)):
    student_scores[score] = int(student_scores[score])
    
    
highest_score = 0
for score in student_scores:
    
    if score > highest_score:
        highest_score = score
        
print(f" The highest score is {highest_score}")
        

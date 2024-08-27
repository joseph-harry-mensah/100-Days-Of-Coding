#This program collects the height of students as input
# then finds the average height among the students





#Collecting user input
student_height = input("Enter the heights of each student").split()




# using a range from 0 to the len of the heights to convert break the into 
# a list and convery them to int dtype

for height in range(0, len(student_height)):
    student_height[height] = int(student_height[height])
    
    
    
 # initializing the total height as 0  and writing a fuction to add heights one after the other
# and divided by the len of the student heights


total_height = 0

for height in student_height:
    total_height += height
    
    
    
    # calculating the total number of students 
number_of_student = 0
for student in student_height:
    student += 1
    
    
    # Working out the average
average_height = round(total_height / len(student_height), 1)

    
    
message = f"The average height of the students is {average_height}cm"
print(message)
    
#This calculates the number of paint needed to paint a wall
# 1 can of paint covers 5 square meters of a wall


import math  # Will use the .ceil round it to a whole number




# creating a function with the three parameters needed
def message(height, width, cover): 
    area = height * width          
    num_paint_cans = math.ceil(area / cover)
    
    print(f"You'll need {num_paint_cans} cans of paint") # Our print format
    

    # Taking inputs
heights = int(input("What is the height of the wall?\n"))
widths = int(input("What is the width of the wall?\n"))
covers = 5   
   
    
    # Message output
message(height = heights, width = widths, cover = covers)
    
    
    
    
import tkinter as tk
from random import seed
from random import randint

#Create the main window
root = tk.Tk()
root.title("Random Hidden List")
root.minsize(800, 600)

# Create an empty list
empty_list = []

# The seed function is used to help create the randomly generated numbers. 
#Further explanation found here: https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
seed(1)
for i in range(100): #This range will dictate how long the list will be. It will have 100 random numbers in a list
    rand_range = randint(0, 100) #randint sets the range for the random numbers. Here it can be any number between 0 and 100 and its assigned the rand_range variable
    empty_list.append(rand_range) #append the values to the empty list
    new_random_list = empty_list # reassign the empty list to a variable that makes sense.

#Create a labels
#user_label will prompt the user for an input.
user_label = tk.Label(root, text="Enter an integer and see if its in our randomized list")
user_label.pack(pady=0)

# Label to show the user that their number is in the list. Label will become visible after they enter a number
list_label = tk.Label(root, text ="")
list_label.pack()

#Textbox for user input
textbox = tk.Entry(root)
textbox.pack(pady=10)

# Create a canvas to draw the colored boxes
canvas = tk.Canvas(root, width=600, height=100)
canvas.pack(pady=20)

# Initialize rectangle IDs
rectangles = []

# This function will search through the randomized list and check if the user input is in the list.
def find_num_inlist():
    user_input = int(textbox.get())
    print(f"User Input: {user_input}")#Test prints for the terminal
    print(f"new_random_list: {new_random_list}")#Test prints for the terminal
    
    #Clear canvas
    canvas.delete("all")

    # Create and iterate through list and highlight rectangles.
    for index, value in enumerate(new_random_list):
        x1 = 1 + index * 5  # Adjust these values to position the rectangles
        x2 = x1 + 5
        y1 = 50
        y2 = 100
        # color = "yellow"
        if value == user_input:
            color = "green"
        else:
            color = "red"
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        rectangles.append(color)
    
    if user_input in new_random_list:
        list_label.config(text=f"Your number {user_input} is in the list")
    else:
        list_label.config(text=f"Your number {user_input} is not in the list")


# Create buttons
# button1 will execute the find_num_inlist function
button1 = tk.Button(root, text="Display List", command=find_num_inlist)
button1.pack(pady=30)



# This code creates a non random list from 1 to 100
# for i in range(1,101):
#     empty_list.append(i)
#     new_list = empty_list
#print(new_list)

root.mainloop()
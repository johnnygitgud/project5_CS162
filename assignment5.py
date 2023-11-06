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

print(new_random_list)#Test print random list in terminal

#Create a labels
#user_label will prompt the user for an input.
user_label = tk.Label(root, text="Enter an integer and see if its in our randomized list")
user_label.pack(pady=0)

list_label = tk.Label(root, text ="")
list_label.pack()

#Textbox for user input
textbox = tk.Entry(root)
textbox.pack(pady=10)

# this loop is to test that an element is in the random list
# for i in new_random_list:
# 	if(i == 17):
# 		print("Element Exists")

# This label for the list needs to appear after the button is clicked. This function will take the new list add it as text to a separate label
def display_list():
    user_input = int(textbox.get())
    print(f"User Input: {user_input}")
    print(f"new_random_list: {new_random_list}")
    
    if user_input in new_random_list:
        list_label.config(text=f"Your number {user_input} is in the list")
    else:
        list_label.config(text=f"Your number {user_input} is not in the list")

            
    
    # if:
    #     list_label = tk.Label(root, text = "This number is not in the list")
    #     list_label.pack()


# Create buttons
# button1 will use the display_list function and show the new random list on a  label below the user label
button1 = tk.Button(root, text="Display List", command=display_list)
button1.pack(pady=30)

######MISSING CODE#######
## I NEED A TEXT BOX FOR USER INPUT
## I NEED A SORT FUNCTION THAT WILL TAKE THE USER INPUT AND CHECK IF ITS IN THE LIST
## ANOTER BUTTON NEEDS TO USE THAT NEW SORT FUNCTION
## I NEED A COLOR OBJECT TO SHOW WHETHER IF THE NUMBER THE USER ENTERED IS IN THE LIST 
## A SEPEARTE COLOR OBJECT IF IT IS WRONG



# This code creates a non random list from 1 to 100
# for i in range(1,101):
#     empty_list.append(i)
#     new_list = empty_list
#print(new_list)

root.mainloop()
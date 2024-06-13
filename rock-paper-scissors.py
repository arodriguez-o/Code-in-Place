import tkinter as tk
from tkinter import *
from time import time
from PIL import Image, ImageTk
import random

#DEFINE MAIN VARIABLES
round_number = 1
computer_choices_list = ["Rock", "Paper", "Scissors"] #LIST OF COMPUTER CHOICES   
user_score = 0 
computer_score = 0

#PLAYER'S CHOICES
def rock_clicked():
    user_choice = "Rock"
    game(user_choice)
def paper_clicked():
    user_choice = "Paper"
    game(user_choice)
def scissors_clicked():
    user_choice = "Scissors"
    game(user_choice)

#MAIN GAME FUNCTION
def game(user_choice):
    #set as global to change variables defined outside function
    global rock_img, paper_img, scissors_img, thumbs_down_img, thumbs_up_img, correct_img, resized_correct_img, incorrect_img, resized_incorrect_img, equal_img, victory, defeat #Images
    global round_number, user_score, computer_score #Scores
    global score_text, top_text #Texts

    #hide buttons once choice is made
    rock_button.pack()
    paper_button.pack()
    scissors_button.pack()

    #computer's pick
    computer_choice = random.choice(computer_choices_list)

    #show choices in canvas
    if user_choice == "Rock":
        user_img = canvas.create_image(200,400, image=rock_img)
    elif user_choice == "Paper":
        user_img = canvas.create_image(200,400, image=paper_img)
    elif user_choice == "Scissors":
        user_img = canvas.create_image(200,400, image=scissors_img)
    
    if computer_choice == "Rock":
        computer_img = canvas.create_image(600,400, image=rock_img)
    elif computer_choice == "Paper":
        computer_img = canvas.create_image(600,400, image=paper_img)
    elif computer_choice == "Scissors":
        computer_img = canvas.create_image(600,400, image=scissors_img)
    ###############################

    #compare choices
    if user_choice == computer_choice:
        #### pick again message #####
        # print("pick again")
        result = canvas.create_image(400,200, image=equal_img)
    elif (user_choice == "Rock") and (computer_choice == "Paper"):
        ### you lose! ###
        computer_score = computer_score + 1
        round_number = round_number + 1
        result = canvas.create_image(400,200, image=thumbs_down_img)
    elif (user_choice == "Rock") and (computer_choice == "Scissors"):
        ### you win! ###
        user_score = user_score + 1
        round_number = round_number + 1
        result = canvas.create_image(400,200, image=thumbs_up_img)
    elif (user_choice == "Paper") and (computer_choice == "Rock"):
        ### you win! ###
        user_score = user_score + 1
        round_number = round_number + 1
        result = canvas.create_image(400,200, image=thumbs_up_img)
    elif (user_choice == "Paper") and (computer_choice == "Scissors"):
        ### you lose ###
        computer_score = computer_score + 1
        round_number = round_number + 1
        result = canvas.create_image(400,200, image=thumbs_down_img)
    elif (user_choice == "Scissors") and (computer_choice == "Paper"):
        ### you win! ###
        user_score = user_score + 1
        round_number = round_number + 1
        result = canvas.create_image(400,200, image=thumbs_up_img)
    elif (user_choice == "Scissors") and (computer_choice == "Rock"):
        ### you lose ###
        computer_score = computer_score + 1
        round_number = round_number + 1
        result = canvas.create_image(400,200, image=thumbs_down_img)
    
    def delete_images():
        canvas.delete(user_img)
        canvas.delete(computer_img)
        canvas.delete(result)
    def victory_screen():
        rock_button.destroy()
        paper_button.destroy()
        scissors_button.destroy()
        delete_images()
        canvas.itemconfig(top_text, text = "Congratulations, you win!")
        canvas.create_image(400,400,image=victory)
    def defeat_screen():
        rock_button.destroy()
        paper_button.destroy()
        scissors_button.destroy()
        delete_images()
        canvas.itemconfig(top_text, text = "Better luck next time!")
        canvas.create_image(400,400,image=defeat)

    #Check if there's a winner in this round
    if user_score == 5:
        root.after(2000, victory_screen)
        canvas.itemconfig(score_text, text="Your score: " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
    elif computer_score == 5:
        root.after(2000, defeat_screen)
        canvas.itemconfig(score_text, text="Your score: " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
    else:
        root.after(3000, place_buttons)
        root.after(3000, change_round)
        root.after(3000, delete_images)
        canvas.itemconfig(score_text, text="Your score: " + str(user_score) + "\n" + "Computer's score: " + str(computer_score))
           
#SETTING UP CANVAS
root = tk.Tk()
canvas = tk.Canvas(root, bg="white", width=800, height=800) #Create canvas
canvas.pack(fill="both", expand=True) 
upper_text = "WELCOME TO ROCK, PAPER, SCISSORS!" #Set upper text to welcome

img = PhotoImage(file = "rock-paper-scissors.png") #Set main image

rock_img = PhotoImage(file = "ROCK.png")
paper_img = PhotoImage(file = "PAPER.png")
scissors_img = PhotoImage(file = "SCISSORS.png")

correct_img = Image.open("good.png")
resized_correct_img = correct_img.resize((100,100))
thumbs_up_img = ImageTk.PhotoImage(resized_correct_img)
incorrect_img = Image.open("bad.png")
resized_incorrect_img = incorrect_img.resize((100,100))
thumbs_down_img = ImageTk.PhotoImage(resized_incorrect_img)
equal_img = PhotoImage(file="equal.png")
victory = PhotoImage(file="victory.png")
defeat = PhotoImage(file="defeat.png")

top_text = canvas.create_text((400, 50), text=upper_text, font=("Arial", 20), fill='black') #Create upper text
main_image = canvas.create_image(400,400,image=img) #Create main image
bottom_text = canvas.create_text((400, 700), text="Select Rock, Paper, or Scissors and try to beat the computer!", font=("Arial", 14), fill = 'black') #Create instructions text
score_text = canvas.create_text((400, 730), text="")


#DEFINE BUTTONS
rock_button = Button(root, image=rock_img, command=rock_clicked, cursor="hand2", width=200, height=300)
paper_button = Button(root, image=paper_img, command=paper_clicked, cursor="hand2", width=200, height=300)
scissors_button = Button(root, image=scissors_img, command=scissors_clicked, cursor="hand2", width=200, height=300)

def button_clicked():
    #CLEAR WELCOME, INSTRUCTIONS, AND START BUTTON
    canvas.itemconfig(top_text, text="Choose Rock, Paper, or scissors:")
    change_round()
    canvas.delete(main_image)
    start_button.destroy()
    place_buttons()

#START BUTTON
start_button = Button(root, text="Start", command=button_clicked, cursor="hand2", width=20)
start_button.place(x=320, y=720)

#PLACE BUTTONS FUNCTION
def place_buttons():       
    rock_button.place(x=10, y=100)        
    paper_button.place(x=300, y=100)        
    scissors_button.place(x=580, y=100)

def change_round():
    canvas.itemconfig(bottom_text, text="Round " + str(round_number))

root.mainloop()
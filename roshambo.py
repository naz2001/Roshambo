from tkinter import *
from tkinter import ttk
import random

#Create an instance of tkinter frame
win= Tk()

win.geometry("500x350")
win.title("ROSHAMBO")

#Default value for Computer
computer_options = {"0":"Rock", "1":"Paper","2":"Scissor"}

#Disable all the Buttons after first Match
def button_disable():
   b1.config(state= "disabled")
   b2.config(state= "disabled")
   b3.config(state= "disabled")

#function for Rock
def rock():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Draw"
   elif value=="Scissors":
      match_result = "You Won!!!"
   else:
      match_result = "Computer Wins"
   label1.config(text = match_result)
   l1.config(text = "Rock")
   l3.config(text =  value)
   button_disable()

#function for Paper
def paper():
   value = computer_options[str(random.randint(0, 2))]
   if value == "Paper":
      match_result = "Draw"
   elif value=="Scissor":
      match_result = "Computer Wins"
   else:
      match_result = "You won!!!"
   label1.config(text = match_result)
   l1.config(text = "Paper")
   l3.config(text = value)
   
   button_disable()

#Function for Scissor
def scissors():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Computer Wins"
   elif value == "Scissors":
      match_result = "Draw"
   else:
      match_result = "You Win!!!"
   label1.config(text = match_result)
   l1.config(text = "Scissors")
   l3.config(text = value)
   button_disable()

#Reset the Game
def reset():
   b1.config(state= "active")
   b2.config(state= "active")
   b3.config(state= "active")
   l1.config(text = "You")
   l3.config(text = "Computer")
   label1.config(text = "")

#Create a LabelFrame
labelframe= LabelFrame(win, text= "ROSHAMBO", font=('Comic Sans MS', 24, 'bold italic'),labelanchor= "n",bd=10,bg= "#703456", cursor= "target")
labelframe.pack(expand= True, fill= BOTH)

label1= Label(labelframe, text="", font=('Comic Sans MS', 22, 'bold italic'),bg= "#703456",justify= CENTER,fg="white")
label1.place(relx= .4, rely= .4)


l1= Label(labelframe, text="You", font= ('Comic Sans MS', 18, 'bold '),bg= "#703456",fg="white")
l1.place(relx= .17, rely= .2)

l2= Label(labelframe, text="VS", font= ('Comic Sans MS', 22, 'bold italic'),bg= "#703456")
l2.place(relx= .45, rely= .2)

l3= Label(labelframe, text="Computer", font= ('Comic Sans MS', 18, 'bold'),bg= "#703456",fg="white")
l3.place(relx= .70, rely= .2)


b1= Button(labelframe, text= "Rock", font= 10, width= 7, command= rock, bg='#f5e4ed',borderwidth = 5)
b1.place(relx=.22, rely= .62)
b2= Button(labelframe, text= "Paper", font= 10, width= 7 ,command= paper,bg='#f5e4ed',borderwidth = 5)
b2.place(relx= .41,rely= .62)
b3= Button(labelframe, text= "Scissor", font= 10, width= 7, command= scissors,bg='#f5e4ed',borderwidth = 5)
b3.place(relx= .60, rely= .62)

#Button to reset the Game
reset= Button(labelframe, text= "Reset",bg= "OrangeRed3", fg= "white", font= 10, width= 7, command= reset)
reset.place(relx= .41, rely= .82)
win.mainloop()

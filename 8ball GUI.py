
import tkinter
from tkinter import *
import time
import random
import sys
import queue

#Different answers
answerList = []
answerList.append("Maybe") #1
answerList.append("Please don't") #2
answerList.append("Try again") #3
answerList.append("Yeah right") #4
answerList.append("NO!")  #5
answerList.append("Go for it!") # 6
answerList.append("Yeah!!!") #7
answerList.append("Absolutely") #8`
answerList.append("Nah") #9
answerList.append("Uh huh") #10


answerList.append("Not Really") #11
answerList.append("YES!") #12
answerList.append("Perhaps") #13
answerList.append("Think about it") #14
answerList.append("Not at all")  #15
answerList.append("Don't even") # 16
answerList.append("Don't question it") #17
answerList.append("You better") #18
answerList.append("Definitely") #19
answerList.append("Sometimes") #20

#Widget code
root = Tk()
root.minsize(width = 300, height = 200)
#Question Label

qLabel = Label(root, text = "Enter a question")
qLabel.grid(row = 0, sticky = W )

#Question textbox
qBox = Entry(root, bd = 5)
qBox.grid(row = 0,  column = 1)



#Now loading/Answer Label
loadTxt = StringVar()
loadLabel = Label(root, textvariable = loadTxt)
loadLabel.grid(row = 3, sticky = S)



#Answers
aTxt = StringVar()
aLabel = Label(root, textvariable = aTxt)
aLabel.grid (row = 5, column = 2)


#Functions
#Set timer
def sleepLoad():
        loadTxt.set("Now Loading..")
        seconds = 5
        time.sleep(seconds)
        aTxt.set(random.choice(answerList))



#Clear textbox
def clear():
 qBox.delete(0,END)

#quit
def quit():
    sys.exit(0)

#Submit Button Function
submitBtn = Button(text = "Ask", command = sleepLoad)
submitBtn.grid(row = 0, column = 3)

#Clear Button Function
clearBtn = Button (text = "Clear", command = clear)
clearBtn.grid(row = 2, column = 1)


#Quit Button
quitBtn = Button(text= "Exit", command = quit)
quitBtn.grid(row = 2, column = 2)
root.mainloop()

#Play Again Button

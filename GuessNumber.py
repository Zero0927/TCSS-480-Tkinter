import sys
import random
import re
import tkinter as tk

flag = True
number = 0
num = random.randint(0,1024)
maxnumber = 1024
minnumber = 0
#Siyuan Zhou(Scott)
def Close(event):
    root.destroy()

def Guessing(event):
    global flag
    global number
    global num
    global maxnumber
    global minnumber
    if flag:
        input = int(input_a.get())
        if input == num:
            resultprint(" Congratualations, it is correct! ")
            number += 1
            flag = False
            GuessNumber()
        elif input < num:
            if input > minnumber:
                minnumber = input
                number +=1
                tip_min.config(tip_min,text=minnumber)
            resultprint("Too small")
        else:
            if input < maxnumber:
                maxnumber = input
                number +=1
                tip_max.config(tip_max,text=maxnumber)
            resultprint("Too big")
    else:
        resultprint("You already got it..")

def resultprint(TextV):
    label_val_q.config(label_val_q,text=TextV)

def GuessNumber():
    if number == 1:
        resultprint(" Correct on the first attempt")
    elif number < 10:
        resultprint(" Try to get it right within 10 attempts: " +str(number))
    elif number < 50:
        resultprint(" Attempt times: " + str(number))
    else:
        resultprint(" It is over 50 attempts.... Attemp times: " + str(number))

root = tk.Tk(className = "Guess Number Game")
root.geometry("450x100+700+400")

line_a_tip = tk.Frame(root)
tip_max = tk.Label(line_a_tip,text=maxnumber)
tip_min = tk.Label(line_a_tip,text=minnumber)
tip_max.pack(side = "top", fill = "x")
tip_min.pack(side = "bottom", fill = "x")
line_a_tip.pack(side = "left", fill = "y")

line_question = tk.Frame(root)
label_val_q = tk.Label(line_question,width="80")
label_val_q.pack(side="left")
line_question.pack(side="top",fill="x")

line_input = tk.Frame(root)
input_a = tk.Entry(line_input,width="40")
btnGuess = tk.Button(line_input,text="Guess")
input_a.pack(side = "left")
input_a.bind('<Return>',Guessing)
btnGuess.bind('<Button-1>',Guessing)
btnGuess.pack(side="left")
line_input.pack(side = "top", fill = "x")

line_btn = tk.Frame(root)
btnClose = tk.Button(line_btn,text="Close")
btnClose.bind('<Button-1>',Close)
btnClose.pack(side="left")
line_btn.pack(side="top")

resultprint(" Please enter any integer from 0 to 1024: ")
print(num)
root.mainloop()

            
        
        
        

import tkinter
import random

score = 0
timeleft = 30

colors = ["Pink","Blue","Black","Yellow", "Orange","Red","Purple","Green"]


def startgame(event):
    global timeleft

    if timeleft == 30:
        countdown()
    nextcolor()


def nextcolor():

    global colors
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()
        
        if e.get().lower() == colors[1].lower():
            score += 1

        e.delete(0, tkinter.END)
        
        random.shuffle(colors)
        label.config(fg = str(colors[1]),text = str(colors[0]))
        scoreLabel.config(text = 'Score : ' + str(score))

def countdown():

    global timeleft

    if timeleft > 0:
        timeleft -= 1

    timeLabel.config(text = 'Time Left : ' + str(timeleft))

    timeLabel.after(1000, countdown)

#driver code

app = tkinter.Tk()

app.title('ColorGuess')

app.geometry('375x200')

instruction = tkinter.Label(app, text = 'Type the color of the words and not the word text!', font = ('Helvetica',12))
instruction.pack()

scoreLabel = tkinter.Label(app, text = 'Press enter to start', font = ('Helvetica',12))
scoreLabel.pack()

timeLabel = tkinter.Label(app, text = 'Time Left: ' + str(timeleft),font = ('Helvetica',12))
timeLabel.pack()

label = tkinter.Label(app, font = ('Helvetica',60))
label.pack()

e = tkinter.Entry(app)

app.bind('<Return>', startgame)
e.pack()

e.focus_set()

app.mainloop()
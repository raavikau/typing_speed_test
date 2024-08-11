import csv
import random
from tkinter import *

background = 'gold2'
foreground = 'red'
sliderwords = ''
timeleft = 60
completed_word = set()
count = index = wpm_count = correct = wrong = 0
word_list = []

def load_word_list():
    with open('words.csv') as word_data:
        data = csv.reader(word_data)
        for row in data:
            word_list.append(''.join(row))
        random.shuffle(word_list)

def slider():
    global sliderwords, count
    text = 'Welcome to Typing Speed Game'
    if count >= len(text):  # start the slider from zero after once complete
        count = 0
        sliderwords = ''
    sliderwords = sliderwords + text[count]  # text moves by adding one character
    movingLabel.config(text=sliderwords)
    count += 1
    movingLabel.after(200, slider)  # calls itself every 200 milli sec

def play_game(event):  # Trigger when press Enter
    global wpm_count, correct, wrong, index
    wpm_count += 1
    wordCount.config(text=wpm_count)
    if timeleft == 60:
        timer()
    if wordEntry.get() == wordList['text']:
        correct += 1
    else:
        wrong += 1
    index += 1
    if index < len(word_list)-1:  # if all words used from file
        wordList.config(text=word_list[index])
        wordEntry.delete(0, END)
    else:
        wordList.config(text="All words used!")
        wordEntry.config(state=DISABLED)

def timer():
    global timeleft
    if timeleft > 0:
        timeleft -= 1  # decrease time counter
        timeCounter.config(text=timeleft)
        timeCounter.after(1000, timer)
    else:
        wordList.config(state=DISABLED)
        wordEntry.config(state=DISABLED)  # to disable entry field when times up
        instructionLabel.config(text=f"Correct Words {correct} WPM\nWrong Words {wrong}")

window = Tk()
window.title('Speed Typing Test')
window.geometry('700x500')
window.config(bg=background)

movingLabel = Label(text='', bg=background, fg=foreground, font=('ariel', 25, 'bold italic'), width=35)
movingLabel.place(x=0, y=10)
slider()
wordCount = Label(text=wpm_count, width=3, font=('ariel', 20, 'normal'))
wordCount.config(padx=10, pady=10)
wordCount.place(x=190, y=100)
wordLabel = Label(text='word', bg=background, font=('ariel', 23, 'bold'))
wordLabel.place(x=190, y=150)
timeCounter = Label(text=timeleft, width=3, font=('ariel', 20, 'normal'))
timeCounter.config(padx=10, pady=10)
timeCounter.place(x=450, y=100)
timeLabel = Label(text='timer', bg=background, font=('ariel', 23, 'bold'))
timeLabel.place(x=450, y=150)

load_word_list()
wordList = Label(text=word_list[index], width=18, bg=background, font=('ariel', 23), justify=CENTER)
wordList.place(x=200, y=220)
wordEntry = Entry(font=('ariel', 20), justify=CENTER)
wordEntry.focus_set()  # set the cursor
wordEntry.place(x=200, y=260)
instructionLabel = Label(text='Type word and Hit Enter', fg=foreground, bg=background, font=('ariel', 22))
instructionLabel.place(x=220, y=310)
window.bind('<Return>', play_game)  # binds the Enter key to play_game func

window.mainloop()

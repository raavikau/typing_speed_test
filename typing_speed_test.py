from tkinter import *
import random
word_list = ['Difficult', 'Trouble', 'Worthy', 'Gold', 'Six', 'radio', 'Will you', 'Second', 'Future', 'Burn', 'General', 'Empty', 'Decision',
             'Others', 'motion', 'Control', 'Serious', 'eyes', 'move', 'Atom', 'rights', 'Missing', 'Clothes', 'Target', 'Quick', 'during']

background = 'gold2'
foreground = 'red'
sliderwords = ''
timeleft = 60
count = wpm_count = correct = wrong = 0
def slider():
    global sliderwords, count
    text = 'Welcome to Typing Speed Game'
    if count >= len(text):
        count = 0
        sliderwords = ''
    sliderwords = sliderwords + text[count]
    movingLabel.config(text=sliderwords)
    count += 1
    movingLabel.after(200, slider)

def play_game(event):
    global wpm_count, correct, wrong
    wpm_count += 1
    wordCount.config(text=wpm_count)
    if timeleft == 60:
        timer()
    if wordEntry.get() == wordList['text']:
        correct += 1
    else:
        wrong += 1
    random.shuffle(word_list)
    wordList.config(text=word_list[0])
    wordEntry.delete(0, END)

def timer():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeCounter.config(text=timeleft)
        timeCounter.after(1000, timer)
    else:
        wordEntry.config(state=DISABLED)
        instructionLabel.config(text=f"Correct Words {correct}\nWrong Words{wrong}")
window = Tk()
window.title('Speed Typing Test')
window.geometry('700x500')
window.config(bg=background)

movingLabel = Label(text='', bg=background, fg=foreground, font=('ariel', 25, 'bold italic'), width=35)
movingLabel.place(x=0, y=10)
slider()
wordCount = Label(text=wpm_count, font=('ariel', 20, 'normal'))
wordCount.config(padx=10, pady=10)
wordCount.place(x=200, y=100)
wordLabel = Label(text='word', bg=background, font=('ariel', 23, 'bold'))
wordLabel.place(x=190, y=150)
timeCounter = Label(text=timeleft, font=('ariel', 20, 'normal'))
timeCounter.config(padx=10, pady=10)
timeCounter.place(x=450, y=100)
timeLabel = Label(text='timer', bg=background, font=('ariel', 23, 'bold'))
timeLabel.place(x=440, y=150)
random.shuffle(word_list)
wordList = Label(text=word_list[0], bg=background, font=('ariel', 23))
wordList.place(x=300, y=220)
wordEntry = Entry(font=('ariel', 20), justify=CENTER)
wordEntry.focus_set()
wordEntry.place(x=200, y=260)
instructionLabel = Label(text='Type word and Hit Enter', fg=foreground, bg=background, font=('ariel', 22))
instructionLabel.place(x=220, y=310)
window.bind('<Return>', play_game)

window.mainloop()

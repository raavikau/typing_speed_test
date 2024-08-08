from tkinter import *
background = 'gold2'
foreground = 'red'

window = Tk()
window.title('Speed Typing Test')
window.geometry('700x500')
window.config(bg=background)

movingLabel = Label(text='Welcome to Typing Speed Game', bg=background, fg=foreground, font=('ariel', 25, 'bold italic'), width=35)
movingLabel.place(x=0, y=10)
wordCount = Label(text='0', font=('ariel', 20, 'normal'))
wordCount.config(padx=10, pady=10)
wordCount.place(x=200, y=100)
wordLabel = Label(text='word', bg=background, font=('ariel', 23, 'bold'))
wordLabel.place(x=190, y=150)
timeCounter = Label(text='0', font=('ariel', 20, 'normal'))
timeCounter.config(padx=10, pady=10)
timeCounter.place(x=450, y=100)
timeLabel = Label(text='timer', bg=background, font=('ariel', 23, 'bold'))
timeLabel.place(x=440, y=150)
wordList = Label(text='Testing', bg=background, font=('ariel', 25))
wordList.place(x=300, y=220)
wordEntry = Entry(font=('ariel', 20, 'bold'), justify=CENTER)
wordEntry.focus_set()
wordEntry.place(x=200, y=260)
instructionLabel = Label(text='Type word and Hit Enter', fg=foreground, bg=background, font=('ariel', 22))
instructionLabel.place(x=220, y=310)

window.mainloop()

from tkinter import *
import random
word_list = ['Difficult', 'Trouble', 'Worthy', 'Gold', 'Six', 'radio', 'Will you', 'Second', 'Future', 'Burn', 'General', 'Empty', 'Decision',
             'Others', 'motion', 'Control', 'Serious', 'eyes', 'move', 'Atom', 'rights', 'Missing', 'Clothes', 'Target', 'Quick', 'Disposant','during',
             'Let go', 'Beat', 'In addition', 'princess', 'just', 'Dreams', 'Advice', 'Everyone', 'Anton', 'Mine', 'Love', 'Behaviour', 'Thinking',
             'Divya', 'human being', 'local', 'Trouble', 'Move', 'Panting', 'Appreciate', 'Soldier', 'visit']

sliderwords = ''
count = 0
i = 0
def slider():
    global sliderwords, count
    text='Welcome to Typing Speed Game'
    if count >= len(text):
        count = 0
        sliderwords = ''
    sliderwords = sliderwords+text[count]
    movingLabel.config(text=sliderwords)
    count += 1
    movingLabel.after(200, slider)
def play_game(event):
    global i
    i += 1
    word_count.config(text=i)
    wordEntry.delete(0, END)
    random.shuffle(word_list)
    wordLabel.config(text=word_list[0])

root = Tk()
root.title('Speed Typing Test')
root.geometry('700x500+250+50')
root.config(bg='gold2')
movingLabel = Label(text='', bg='gold2', fg='red', font=('ariel', 25, 'bold italic'), width=35)
movingLabel.place(x=0, y=10)
slider()
word_count = Label(text=i, font=('ariel', 20, 'normal'))
word_count.config(padx=10, pady=10)
word_count.place(x=200, y=140)
words = Label(text='words', bg='gold2', font=('ariel', 18, 'normal'))
words.place(x=190, y=200)
time_count = Label(text='60', font=('ariel', 20, 'normal'), justify=CENTER)
time_count.config(padx=10, pady=10)
time_count.place(x=450, y=140)
time_label = Label(text='timer', bg='gold2', font=('ariel', 18, 'normal'))
time_label.place(x=450, y=200)
random.shuffle(word_list)
wordLabel = Label(text=word_list[0], bg='gold2', font=('ariel', 30, 'italic bold'), justify=CENTER)
wordLabel.place(x=300, y=250)
wordEntry = Entry(font=('ariel', 15, 'bold'), justify=CENTER)
wordEntry.focus_set()
wordEntry.place(x=230, y=300)

root.bind('<Return>', play_game)
root.mainloop()

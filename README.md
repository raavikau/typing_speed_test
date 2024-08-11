## Typing Speed Test implementation in python using tkinter 
### Initialize State
* Read the word from CSV file append words into list and shuffle the list.
* Set up the Tkinter window with title and specific dimensions.
* Set the word count to 0 and timer of 60 minute.
### Running State
* Function repeatedly calls itself every 200ms and create the moving effects of the welcome message.
* User type word in entry box that picks from word_list and press enter.
* The game checks the word is correct, move to next word and update score
* Timer starts the countdown when you press enter and also clear the entry box.
### Terminal State
* When all the words in list have been use or time counter is equal to zero the game ends.
* Disable the entry box and display the total number of correct and wrong words.

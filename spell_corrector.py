import tkinter as tk
from textblob import TextBlob


# function to get corrected word
def correction():
	# get a content from entry box
	input_word = word1_field.get()

	# creates a TextBlob object
	blob_obj = TextBlob(input_word)

	# get corrected word
	corrected_word = str(blob_obj.correct())
	word2_field.insert(10, corrected_word)

# function to clear text from entry boxes
def clearAll():
	word1_field.delete(0, tk.END)
	word2_field.delete(0, tk.END)


# main program
if __name__ == '__main__':

	root = tk.Tk()

	root.configure(background='white') # white background
	root.geometry('400x200') # window size
	root.title('Spell Corrector') 

	# creates the labels 
	input_label = tk.Label(root, text='Input Word:', fg='black',font=('Times', '20'), bg='light grey')
	corrected_label = tk.Label(root, text='Corrected Word:', fg='black',font=('Times', '18') ,bg='light grey')

	# grid method -> arranges label's locations
	input_label.grid(row=1, column=0)
	corrected_label.grid(row=3, column=0, padx=15)

	# creates text entry box
	word1_field = tk.Entry()
	word2_field = tk.Entry()

	# arranges location of entry boxes 
	word1_field.grid(row=1, column=1, padx=10, pady=15)
	word2_field.grid(row=3, column=1, padx=10, pady=15)

	# creates correction buttion -> correct command
	button1 = tk.Button(root, text='Correct', fg='black', command=correction)

	# creates clear buttion -> clear command
	button2 = tk.Button(root, text='Clear', fg='black', command=clearAll)
	
	button1.grid(row=2, column=1)
	button2.grid(row=4, column=1)

	
	root.mainloop()

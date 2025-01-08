from textblob import TextBlob
from tkinter import *

def Auto_Correct():
    # Clear the output box and correct the input text
    Output_text.delete(1.0, END)
    text = input_text.get(1.0, END).strip()
    corrected_text = TextBlob(text).correct()
    Output_text.insert(END, corrected_text)

def Clear():
    # Clear both input and output boxes
    input_text.delete(1.0, END)
    Output_text.delete(1.0, END)

# Main application window setup
root = Tk()
root.title("Auto Correct")
root.geometry('800x500')
root.resizable(False, False)

# Title label
Label(root, text='Auto Correct Text', font=('arial', 20, 'bold'), pady=10).pack()

# Frame for input and output sections
frame = Frame(root, padx=20, pady=10)
frame.pack(fill=BOTH, expand=True)

# Input section
Label(frame, text='Enter Text:', font=('arial', 14)).grid(row=0, column=0, sticky='w', padx=5, pady=5)
input_text = Text(frame, font=('arial', 12), height=10, width=40, wrap=WORD, padx=5, pady=5)
input_text.grid(row=1, column=0, padx=5, pady=5)

# Output section
Label(frame, text='Output:', font=('arial', 14)).grid(row=0, column=1, sticky='w', padx=5, pady=5)
Output_text = Text(frame, font=('arial', 12), height=10, width=40, wrap=WORD, padx=5, pady=5)
Output_text.grid(row=1, column=1, padx=5, pady=5)

# Buttons for actions
btn_frame = Frame(root, pady=10)
btn_frame.pack()

auto_correct_btn = Button(btn_frame, text='Correct', width=15, font=('arial', 12), command=Auto_Correct)
auto_correct_btn.grid(row=0, column=0, padx=10)

clear_btn = Button(btn_frame, text='Clear', width=15, font=('arial', 12), command=Clear)
clear_btn.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()

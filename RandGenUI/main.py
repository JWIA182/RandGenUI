import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# functions
def generate():  
    try:
        number = random.randint(1, int(number_entry.get()))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        
    random_number_box.config(state="normal")
    random_number_box.delete(0, END)
    random_number_box.insert(0, number)
    random_number_box.config(state="readonly")

# root
root = Tk()
root.title("Random Number Generator")
root.geometry("500x350")
root.resizable(False, False)

# entries
random_number_label = Label(root, text="Random Number", font=("Arial", 15))
random_number_box = Entry(root, width=10, font=("Arial", 15), state="readonly")
random_number_label.pack()
random_number_box.pack(pady=20)

number_entry_label = Label(root, text="Enter a number", font=("Arial", 15))
number_entry = Entry(root, width=10, font=("Arial", 15))
number_entry_label.pack()
number_entry.pack(pady=20)


# buttons
generate_button = Button(root, text="Generate Number", width=15, height=2, bg="green", 
                         fg="white", font=("Arial", 15), command=generate)
generate_button.pack(pady=20)


# mainloop
root.mainloop()

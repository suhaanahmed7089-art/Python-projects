# Import tkinter for creating GUI (Graphical User Interface) application
import tkinter as tk

from tkinter import filedialog, messagebox
root=tk.Tk()
root.title("Simple Text Editor")
root.geometry("900x600")

# Creating text area for text editing
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica",12)
)

text.pack(expand=True,fill=tk.BOTH)

# Main Logic

# Function 1 - To create a new file
def new_file():
    text.delete(1.0,tk.END)

# Function 2 - To open a new file
def open_file():
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        # open selected file
        text.delete(1.0,tk.END)
        with open(file_path,"r")as file:
            text.insert(tk.END,file.read())

# Function 3 - To save a file
def save_file():
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))
    messagebox.showinfo("Info","File saved successfully")

# Creating a menu bar
main_menu=tk.Menu(root)
root.config(menu=main_menu)
file_menu=tk.Menu(main_menu)

# Adding options like New File, Open File, Save File and Exit to the Menu bar
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New File",command=new_file)
file_menu.add_command(label="Open File",command=open_file)
file_menu.add_command(label="Save File",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Create a Text widget for text editing
root.mainloop()

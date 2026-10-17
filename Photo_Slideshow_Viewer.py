import tkinter as tk
from PIL import Image,ImageTk
import time

# Main window

root=tk.Tk()
root.geometry("1200x800")
root.title("Photot Slideshow Viewer")

image_path=[
    r"D:\Walpapers\5sIByr_361855.jpg",
    r"D:\Walpapers\5sIByr_361855.jpg",
    r"D:\Walpapers\batman-is-not-a-replacement-he-is-a-revolution-4i.jpg",
    r"D:\Walpapers\batman-the-shadow-du.jpg",
    r"D:\Walpapers\batman-guardian-of-gotham-night-ab.jpg",
    r"D:\Walpapers\the-batman-on-the-hunt-i2.jpg",
    r"D:\Walpapers\goku-born-to-dominate-ko.jpg",
    r"D:\Walpapers\goku-super-saiyan-power-unleashed-r7.jpg",
]
image_size=(1200,650)
images=[]
for path in image_path:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img)

# Convert PIL images to Tkinter compatible images 

final_images=[]
for img in images:
    photo=ImageTk.PhotoImage(img)
    final_images.append(photo)

# Label widget to keep photo

image_label=tk.Label(root)
image_label.pack()

# Slideshow function 
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)       # Delay of 2 seconds between images

play_button=tk.Button(root,text="Start Slideshow",font="Helvetica 15 bold",command=start_slideshow,bg="light grey")
play_button.pack(pady=20,padx=20)

root.mainloop()

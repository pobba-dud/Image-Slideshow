# Import tkinter module
import tkinter
from tkinter import *
from PIL import Image, ImageTk

# Initialize window
root = Tk()
root.attributes('-fullscreen', True)

# Create canvas
canvas = Canvas(root, width=1600, height=900)
canvas.pack()

# Load image
img = Image.open(r"image.jpg")

# Resize image (if needed) using resize method
resized_image = img.resize((1600, 900), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)

# Add image to canvas
canvas.create_image(0, 0, anchor=NW, image=new_image)

# Main loop
root.mainloop()
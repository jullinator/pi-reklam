from tkinter import *

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = Canvas(root, width =screen_width,height=screen_height)
images = {}



def make_image (name, imageUrl):
    images[name] = PhotoImage(file="images/"+imageUrl)

def show_image (name):
    canvas.create_image(0,0, image=images[name])

root.mainloop()

import tkinter
import PIL

from tkinter import *
from PIL import Image,ImageTk


root = Tk()
root.title('mapa')
root.geometry("500x500")

my_canvas = Canvas(root, width=300, height=300, bg="white")
my_canvas.pack(pady=10)

# mriezka zvisle
# my_canvas.create_line(x1, y1, x2, y2, fill="color")
my_canvas.create_line(30, 300, 30, 0, fill="black")
my_canvas.create_line(60, 300, 60, 0, fill="black")
my_canvas.create_line(90, 300, 90, 0, fill="black")
my_canvas.create_line(120, 300, 120, 0, fill="black")
my_canvas.create_line(150, 300, 150, 0, fill="black")
my_canvas.create_line(180, 300, 180, 0, fill="black")
my_canvas.create_line(210, 300, 210, 0, fill="black")
my_canvas.create_line(240, 300, 240, 0, fill="black")
my_canvas.create_line(270, 300, 270, 0, fill="black")

# mriezka rovnomerne
# my_canvas.create_line(x1, y1, x2, y2, fill="color")
my_canvas.create_line(0, 30, 300, 30, fill="black")
my_canvas.create_line(0, 60, 300, 60, fill="black")
my_canvas.create_line(0, 90, 300, 90, fill="black")
my_canvas.create_line(0, 120, 300, 120, fill="black")
my_canvas.create_line(0, 150, 300, 150, fill="black")
my_canvas.create_line(0, 180, 300, 180, fill="black")
my_canvas.create_line(0, 210, 300, 210, fill="black")
my_canvas.create_line(0, 240, 300, 240, fill="black")
my_canvas.create_line(0, 270, 300, 270, fill="black")

#prekazky
# my_canvas.create_rectangle(x1, y1, x2, y2, fill="color")
# rectangle x1, y1 = top left
# rectangle x2, y2 = botoom right
my_canvas.create_rectangle(30, 60, 60, 30, fill="blue")
my_canvas.create_rectangle(60, 60, 90, 30, fill="blue")
my_canvas.create_rectangle(180, 60, 210, 30, fill="blue")

my_canvas.create_rectangle(120, 90, 90, 120, fill="blue")
my_canvas.create_rectangle(150, 90, 120, 120, fill="blue")
my_canvas.create_rectangle(240, 90, 270, 120, fill="blue")

my_canvas.create_rectangle(120, 150, 90, 180, fill="blue")
my_canvas.create_rectangle(150, 150, 120, 180, fill="blue")
my_canvas.create_rectangle(180, 150, 210, 180, fill="blue")
my_canvas.create_rectangle(210, 150, 240, 180, fill="blue")

my_canvas.create_rectangle(180, 180, 210, 210, fill="blue")
my_canvas.create_rectangle(210, 180, 240, 210, fill="blue")

my_canvas.create_rectangle(60, 210, 90, 240, fill="blue")

my_canvas.create_rectangle(150, 240, 120, 270, fill="blue")
my_canvas.create_rectangle(180, 240, 150, 270, fill="blue")

#robot

##Load an image in the script
img= (Image.open("robot.png"))

#Resize the Image using resize method
resized_image= img.resize((30,30))
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
my_canvas.create_image(0,0, anchor=NW, image=new_image)

root.mainloop()

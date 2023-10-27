# import tkinter as tk
# from PIL import Image, ImageTk
# import time
# window = tk.Tk()
# window.title("Image Viewer")
# window.geometry("600x500")

# frame = tk.Frame(window, width=600, height=400)
# frame.pack()

# canvas = tk.canvas(frame, width=600, height=400, bg="white")
# canvas.pack(pady=20)

# Image 1
# file_1 = Image.open('Running.png')
# file_1_size = file_1.resize((100, 100))
# img_1 = ImageTk.PhotoImage(file_1_size)
# img_id=canvas.create_image(50, 50, image=img_1)
# def move_left(event):
#         x=-10
#         y=0
#         canvas.move(img_id,x,y)
# def move_right(event):
#         x=10
#         y=0
#         canvas.move(img_id,x,y)
# def move_up(event):
#         x=0
#         y=-10
#         canvas.move(img_id,x,y)
# def move_down(event):
#         x=0
#         y=10
#         canvas.move(img_id,x,y)

# window.bind('<Up>',move_up)
# window.bind('<Down>',move_down)
# window.bind('<Right>',move_right)
# window.bind('<Left>',move_left)

# # Text
# canvas.create_text(250, 200, text="Game Over", font=("Robus", 60, "bold"), fill="purple")
# canvas.create_oval(150,100,180,130,fill="Blue")
# time_id=canvas.create_text(250,250,text="10:10:10", font=('Robus', 20), fill="Gray")
# def clock():
#     hour=time.strftime("%H:%M:%S")
#     canvas.itemconfig(time_id, text=hour)
# def updateTime():
#     clock()
#     window.after(1000,updateTime)
# window.after(1000,updateTime)
# window.resizable(0, 0)
# window.mainloop()

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("600x500")
window.title("Game")
frame = tk.Frame(window, width=600, height=500)
frame.pack()
canvas = tk.Canvas(frame, width=500, height=400, bg="white")
canvas.pack()

# shape
shape_id = canvas.create_oval(150, 100, 200, 150, fill="black")
# Image 
image_one = Image.open("boy.png")

img_size = image_one.resize((50,50))

image = ImageTk.PhotoImage(img_size)

boy_id = canvas.create_image(50, 50, image=image)
result_id = canvas.create_text(250, 250, text="", font=("bold", 40), fill="red")
def change_color(shape):
    touch=canvas.find_overlapping(shape[0],shape[1],shape[2],shape[3])
    print(touch)
    if len(touch)>1:
        if touch[1]==boy_id:
            canvas.itemconfig(shape_id,fil="green")
            canvas.itemconfig(result_id,text="Game Over")
            canvas.itemconfig(shape[1], state = 'hidden')
def moveLeft(event):
    change_color(canvas.coords(shape_id))
    x = -10
    y = 0
    canvas.move(boy_id, x, y)
    
def moveRight(event):
    change_color(canvas.coords(shape_id))
    x = 10
    y = 0
    canvas.move(boy_id, x, y)

def moveUp(event):
    change_color(canvas.coords(shape_id))
    x = 0
    y = -10
    canvas.move(boy_id, x, y)

def moveDown(event):
    change_color(canvas.coords(shape_id))
    x = 0
    y = 10
    canvas.move(boy_id, x, y)

window.bind("<Left>", moveLeft)
window.bind("<Right>", moveRight)
window.bind("<Up>", moveUp)
window.bind("<Down>", moveDown)

window.mainloop()
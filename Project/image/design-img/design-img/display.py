import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
window = tk.Tk()
window.title("Image Viewer")
window.geometry("600x500")

frame = tk.Frame(window, width=600, height=400)
frame.pack()

canvas = tk.Canvas(frame, width=500, height=400, bg="white")
canvas.pack(pady=20)

# Image 1
file_1 = Image.open('1.png')
file_1_size = file_1.resize((100, 100))
img_1 = ImageTk.PhotoImage(file_1_size)
canvas.create_image(50, 50, image=img_1, )

# Text
canvas.create_text(250, 200, text="Football Game", font=("sportypo", 25, "bold"), fill="purple")

file_2=Image.open('2.png')
file_2_size=file_2.resize((130,130))
image_2=ImageTk.PhotoImage(file_2_size)
canvas.create_image(120,70,image=image_2)

file_3=Image.open('3.png')
file_3_size=file_3.resize((100,130))
img_3=ImageTk.PhotoImage(file_3_size)
canvas.create_image(210,70,image=img_3)

file_4=Image.open('4.png')
file_4_size=file_4.resize((120,110))
image_4=ImageTk.PhotoImage(file_4_size)
canvas.create_image(320,60,image=image_4)

file_5=Image.open('5.png')
file_5_size=file_5.resize((120,110))
image_5=ImageTk.PhotoImage(file_5_size)
canvas.create_image(440,60,image=image_5)


file_6=Image.open('ucl.png')
file_6_size=file_6.resize((50,50))
image_6=ImageTk.PhotoImage(file_6_size)
canvas.create_image(210,240,image=image_6)

file_7=Image.open('fb-b.png')
file_7_size=file_7.resize((50,50))
image_7=ImageTk.PhotoImage(file_7_size)
canvas.create_image(70,280,image=image_7)

canvas.create_text(100, 280, text="Football Game", font=("Robus", 15, "bold"), fill="purple")
canvas.create_text(310, 280, text="VS", font=("sportypo", 20, "bold"), fill="purple")
canvas.create_text(200, 280, text="Football Game", font=("Robus", 15, "bold"), fill="purple")
window.resizable(0, 0)
window.mainloop()
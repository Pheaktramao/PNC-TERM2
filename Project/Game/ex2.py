import tkinter as tk
from tkinter import colorchooser
def draw(event):
    x1=event.x-5
    x2=event.x+5
    y1=event.y-5
    y2=event.y+5
    canvas.create_oval(x1,y1,x2,y2,fill=draw_color, outline='')
def eraser():
    canvas.delete('all')
def choose_color():
    global draw_color
    draw_color=colorchooser.askcolor()[1]
window = tk.Tk()
window.geometry("1000x600")
window.title("whiteboard")
draw_color='pink'
color_size=10
frame = tk.Frame(window, width=1000, height=600)
frame.pack()
canvas = tk.Canvas(frame, width=800, height=500, bg='white')
canvas.pack(pady=30)
color=tk.Button(frame,text="Choose color",command=choose_color)
color.place(x=10,y=10)
btnEraser=tk.Button(frame,text="Enter")
btnEraser.pack()
canvas.bind('<B1-Motion>',draw)
window.mainloop()
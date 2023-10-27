import tkinter as tk
window=tk.Tk()
window.title("Image Viwer")
window.geometry("600x400")
frame=tk.Frame(window,width=600,height=400)
frame.pack()
canvas=tk.Canvas(frame,width=600,height=400)
canvas.pack()
# canvas.create_rectangle(10,10,100,100,tags="rectangle")
# canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="pink")
# def arrow_up(event):
#     canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="blue")
# def arrow_down(event):
#     canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="green")
# def arrow_right(event):
#     canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="red")
# def arrow_left(event):
#     canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="black")
# window.bind('<Up>',arrow_up)
# window.bind('<Down>',arrow_down)
# window.bind('<Right>',arrow_right)
# window.bind('<Left>',arrow_left)
# def chang_color(event):
#     if event.keysym=="g":
#         canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="green")
#     elif event.keysym=="r":
#         canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="red")
#     elif event.keysym=="b":
#         canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="black")
#     elif event.keysym=="y":
#         canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="yellow")
#     elif event.keysym=='p':
#         canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="purple")
#     elif event.keysym=='o':
# canvas.itemconfigure(canvas.find_withtag('rectangle'),fill="orange")
# window.bind("<Key>",chang_color)
rect_id=canvas.create_oval(10,10,100,100,tags="oval")
def move_left():
    if canvas.coords(rect_id)[0]>10:
        canvas.move(rect_id,-10,0)
def move_right():
    if canvas.coords(rect_id)[2]<598:
        canvas.move(rect_id,10,0)
def move_down():
   if canvas.coords(rect_id)[3] < 398:
        canvas.move(rect_id,0, 10)
def move_up():
    if canvas.coords(rect_id)[1]>10:
        canvas.move(rect_id,0,-10)
def move(event):
    if event.keysym=="Up":
        move_up()
    elif event.keysym=="Down":
        move_down()
    elif event.keysym=="Right":
        move_right()
    elif event.keysym=="Left":
        move_left()
window.bind("<Key>",move)
window.mainloop()
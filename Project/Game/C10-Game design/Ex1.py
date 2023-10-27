import tkinter as tk
window=tk.Tk()
window.geometry("500x500")
window.title("Hello world")
#frame
frame=tk.Frame(window,width=500,height=500)
frame.pack()
#Shape
canvas=tk.Canvas(frame,width=500, height=500)
canvas.pack()
# canvas.create_rectangle(10, 10, 100,100)
# result = canvas.create_text(55, 60, text="0", fill="red", font=("bold", 40))
# total=0
# def up(even):
#         global total
#         total+=1
#         canvas.itemconfig(result,text=total)
# def down(even):
#         global total
#         total-=1
#         canvas.itemconfig(result,text=total)
# window.bind('<Up>',up)
# window.bind('<Down>',down)
#canvasx,canvasy
#event.x,event.y
#find_closest
#itemconfigure
# canvas.create_rectangle(10, 10, 100,100,fill="red")
# canvas.create_rectangle(110, 10, 200,100,fill="blue")
# canvas.create_rectangle(210, 10, 300,100,fill="green")
# canvas.create_rectangle(310, 10, 400,100,fill="yellow")
# canvas.create_rectangle(410, 10, 500,100,fill="purple")
# canvas.create_rectangle(10, 110, 100,200,fill="blue")
# canvas.create_rectangle(10, 210, 100,300,fill="green")
# canvas.create_rectangle(10, 310, 100,400,fill="yellow")
# canvas.create_rectangle(10, 410, 100,500,fill="purple")
# canvas.create_rectangle(410, 110,500 ,200,fill="purple")
# canvas.create_rectangle(410, 210, 500,300,fill="purple")
# canvas.create_rectangle(410, 310, 500,400,fill="purple")
# canvas.create_rectangle(410, 410, 500,500,fill="purple")
# canvas.create_rectangle(110, 410, 200,500,fill="purple")
# canvas.create_rectangle(210, 410, 300,500,fill="purple")
# canvas.create_rectangle(310, 410, 400,500,fill="purple")
# canvas.create_rectangle(410, 410, 500,500,fill="purple")
# canvas.create_oval(210, 210, 300,300,fill="purple")
# def change_color(event):
#     x=canvas.canvasx(event.x)
#     y=canvas.canvasy(event.y)
#     shape_id= canvas.find_closest(x,y)
#     canvas.itemconfigure(shape_id,fill="orange")
# #     print(shape_id)
# canvas.bind("<Button-1>",change_color)
window.resizable(height=0,width=0)
# canvas.create_oval(10,410,90,500,fill="green")
# canvas.create_oval(100,310,190,400,fill="green")
# canvas.create_oval(200,210,290,300,fill="green")
# canvas.create_oval(300,110,390,200,fill="green")
# canvas.create_oval(400,10,490,100,fill="green")
# canvas.create_rectangle(10,10,90,100,fill="pink")
# canvas.create_rectangle(100,110,190,200,fill="pink")
# canvas.create_rectangle(200,210,290,300,fill="pink")
# canvas.create_rectangle(300,310,390,400,fill="pink")
# canvas.create_rectangle(400,400,490,490,fill="pink")
# canvas.create_rectangle(10,410,90,500,fill="purple")
# canvas.create_rectangle(100,210,190,500,fill="purple")
# canvas.create_rectangle(200,310,290,500,fill="purple")
# canvas.create_rectangle(300,110,390,500,fill="purple")
# canvas.create_rectangle(400,10,490,500,fill="purple")
canvas.create_rectangle(10,310,200,400,fill="teal")
canvas.create_oval(40,210,130,300,fill="teal")
canvas.create_rectangle(210,210,400,300,fill="teal")
canvas.create_rectangle(390,310,490,500,fill="teal")
window.mainloop()
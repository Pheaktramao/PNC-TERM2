import tkinter as tk
import random
window = tk.Tk()
window.geometry("500x500")
# window.attributes('-fullscreen', True)
window.configure(bg="black")
# window.resizable(height=0,width=0)
window.title("Hello world")
frame=tk.Frame(window,width=500,height=500)
frame.pack()
canvas=tk.Canvas(frame,width=500, height=500)
canvas.pack()
total=0
# colors=["red","blue","yellow","green"]
# circle_id=canvas.create_oval(10,10,100,100,fill="orange")
# 
canvas.create_rectangle(10, 10, 100,100,fill="red")
result = canvas.create_text(55, 60, text="0", fill="red", font=("bold", 40))
canvas.itemconfig(result,text=total)
def add():
    for i in range():
        global total
        total+=1
        print(canvas.itemconfig(result,text=total))
    # canvas.itemconfig(circle_id,fill=random.choice(colors))
    # canvas.itemconfig()
btn= tk.Button(window, text="Push Me", command=add)
btn.pack()
def minus():
    for i in range:
        global total
        total-=1
        print(canvas.itemconfig(result,text=total))
    # canvas.itemconfig(circle_id,fill=random.choice(colors))
    # canvas.itemconfig(rect_id)
btn= tk.Button(window, text="Push Me", command=minus)
btn.pack()
# # def ():
    
# #     # canvas.itemconfig(circle_id,fill=random.choice(colors))
# #     # canvas.itemconfig(rect_id)
# # btn= tk.Button(frame,text="Push Me", command=click)
# # btn.pack()

# # print("cicle Id:"+str(circle_id))
# # print("rectangle Id:"+str(rect_id))
for i in range(1,10):
    for j in range(1,10):
        canvas.create_rectangle(10+i*100,10+j*100,100+i*100,100+j*100,fill="red")
window.mainloop()
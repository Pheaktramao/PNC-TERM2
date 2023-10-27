import tkinter as tk
window=tk.Tk()
window.title("Image Viwer")
window.geometry("600x500")
frame=tk.Frame(window,width=600,height=500)
frame.pack()
canvas=tk.Canvas(frame,width=600,height=500,bg="white")
canvas.pack()
shape_id=canvas.create_rectangle(10,10,100,100,fill="pink",outline="")
canvas.create_rectangle(0,400,600,500,fill="black",outline="",tags="walls")
yspeed=10
def check_moveable():
    coord=canvas.coords(shape_id)
    walls=canvas.find_withtag("walls")
    overlap=canvas.find_overlapping(coord[0],coord[1],coord[2],coord[3])
    for wall in walls:
        if wall in overlap:
            return False
    return True
def gravity():
    if check_moveable():
        canvas.move(shape_id,0,8)
        window.after(50,gravity)
gravity()
window.mainloop()
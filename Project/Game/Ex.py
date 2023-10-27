from tkinter import *
window=Tk()
window.title("Alltech-Bouncing ball")
window.resizable(False,False)
WIDTH,HEIGHT=400,300
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
ball=canvas.create_oval(10,10,50,50,fill="red")
xspeed=3
yspeed=3
def moveball():
    global xspeed,yspeed
    canvas.move(ball,xspeed,yspeed)
    (leftPos,topPos,rightPos,bottomPos)=canvas.coords(ball)
    if leftPos<=0 or rightPos>=WIDTH:
        xspeed=-xspeed
    if topPos<=0 or bottomPos>=HEIGHT:
        yspeed=-yspeed
    canvas.after(30,moveball)
canvas.after(30,moveball)
window.mainloop()
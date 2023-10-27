import tkinter as tk
from PIL import Image, ImageTk
window=tk.Tk()
window.title("Image Viewer")
window.geometry("500x400")
frame=tk.Frame(window,width=600,height=400)
frame.pack()
getImageFile=Image.open("masha.png")
Img=ImageTk.PhotoImage(getImageFile)
#label
label=tk.Label(frame,Image=Img)
label.pack
window.resizable(width=0,height=0)
window.mainloop()
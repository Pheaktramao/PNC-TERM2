import tkinter as tk
import time
window = tk.Tk()
window.geometry("800x500")
window.attributes('-fullscreen',True)

window.title("GAME")
window.resizable(False, False)

# frame 
frame = tk.Frame(window)
frame.pack()
#Canvas
canvas = tk.Canvas(window, width=800, height=500)
canvas.pack()
#Load the image
image= tk.PhotoImage(file='bananfram.jpg')
#Set the image as the background
canvas.create_image(0,0,image=image, anchor='nw')
window.mainloop()
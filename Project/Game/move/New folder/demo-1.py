import tkinter as tk
from PIL import Image, ImageTk
#pip install pygame
from pygame import mixer
import time
window = tk.Tk()
window.geometry("800x500")
window.title("Move Shape")
window.resizable(False, False)

# frame 
frame = tk.Frame(window)
frame.pack()

# canvas
canvas = tk.Canvas(frame, width=700, height=400, bg="white")
canvas.pack(pady=20)
img_file = Image.open("actor.png")
img_size = img_file.resize((50, 50))
ball = ImageTk.PhotoImage(img_size)
ball_id = canvas.create_image(30, 30, image=ball)



banana_file1 = Image.open("banana.jpg")
banana_size = banana_file1.resize((30, 30))
banana1 = ImageTk.PhotoImage(banana_size)
shape_ids =canvas.create_image(130,130,image = banana1, tag='banana')

banana_file2 = Image.open("banana.jpg")
banana_size = banana_file2.resize((30, 30))
banana2 = ImageTk.PhotoImage(banana_size)
shape_ids =canvas.create_image(200,260,image = banana2, tag='banana')

banana_file3 = Image.open("banana.jpg")
banana_size = banana_file3.resize((30, 30))
banana3 = ImageTk.PhotoImage(banana_size)
shape_ids =canvas.create_image(300,30,image = banana3, tag='banana')

banana_file4 = Image.open("banana.jpg")
banana_size = banana_file4.resize((30, 30))
banana4 = ImageTk.PhotoImage(banana_size)
shape_ids =canvas.create_image(550,136,image = banana4, tag='banana')

banana_file5 = Image.open("banana.jpg")
banana_size = banana_file5.resize((30, 30))
banana5 = ImageTk.PhotoImage(banana_size)
shape_ids =canvas.create_image(350,350,image = banana5, tag='banana')

banana_file6 = Image.open("banana.jpg")
banana_size = banana_file6.resize((30, 30))
banana6 = ImageTk.PhotoImage(banana_size)
shape_ids = canvas.create_image(30,150,image = banana6, tag='banana')

ban= Image.open("banan.jpg")
ban_size = ban.resize((30, 30))
ban= ImageTk.PhotoImage(ban_size)

text_id = canvas.create_text(500,30, text="Score: ", font=("bold", 16))
score = 0

chili_file = Image.open("chili.jpg")
chili_size = chili_file.resize((50, 50))
chili = ImageTk.PhotoImage(chili_size)
canvas.create_image(180,160,image=chili,tag="chilis")
canvas.create_image(490,150,image=chili,tag="chilis")
canvas.create_image(80,300,image=chili,tag="chilis")

actor2_file = Image.open("actor-2.jpg")
actor2_size = actor2_file.resize((50, 50))
actor_2 = ImageTk.PhotoImage(actor2_size)
def eat_banana():
    coord = canvas.coords(ball_id)
    bananas = canvas.find_withtag("banana")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + ball.width(),coord[1] + ball.height())
    for bn in bananas:
        if bn in overlap:
            return bn
    return 0

def eat_chili():
    coord = canvas.coords(ball_id)
    chilis = canvas.find_withtag("chili")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + ball.width(),coord[1] + ball.height())
    for ch in chilis:
        if ch in overlap:
            return ch
    return 0
def is_movebale():
    coord=canvas.coords(ball_id)
    players=canvas.find_withtag('banana')
    print(coord)
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + ball.width(),coord[1] + ball.height())
    print(overlap)
    print(players)

    for player in players:
        if player in overlap:
            return player
    return 0

def is_border_left():
    return canvas.coords(ball_id)[0] < 30

def is_border_right():
    return canvas.coords(ball_id)[0] > 670

def is_border_top():
    return canvas.coords(ball_id)[1] < 30

def is_border_bottom():
    return canvas.coords(ball_id)[1] > 370

def move_shape(event):
    if event.keysym == "Left" and not is_border_left():
        canvas.move(ball_id, -5, 0)
    elif event.keysym == "Right" and not is_border_right():
        canvas.move(ball_id, 5, 0)
    elif event.keysym == "Up" and not is_border_top():
        canvas.move(ball_id, 0, -5)
    elif event.keysym == "Down" and not is_border_bottom():
        canvas.move(ball_id, 0, 5)
    banana_id =  eat_banana()
    chili_id =  eat_chili()
    if banana_id > 0:
        coord = canvas.coords(banana_id)
        canvas.delete(banana_id)
        canvas.create_image(coord[0], coord[1], image=ban)
        mixer.init() 
        mixer.music.load("sound-3.mp3") 
        mixer.music.play() 
        time.sleep(1)
        mixer.music.stop()
        global score
        score += 1 
        update_score()
    if chili_id > 0:
        coord = canvas.coords(chili_id)
        canvas.delete(chili_id)
        canvas.itemconfigure(ball_id, image=actor_2)
        score -= 1 
        update_score()
def update_score():
    canvas.itemconfig(text_id,text="Score: " + str(score))
window.bind("<Key>", move_shape)
window.mainloop()
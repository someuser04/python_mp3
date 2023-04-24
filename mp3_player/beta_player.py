import tkinter
from tkinter import *
import pygame
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

root = Tk()
root.title('Mp3 player')
root.iconbitmap()
root.geometry("500x400")
#background_image = pygame.image.load("samurai.jpg").convert()
pygame.mixer.init()
def play():
    pygame.mixer.music.load("Lofi - Hip.mp3")
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()
#add background image
def add_pic():
    file = askopenfilename()
    back_pic = ImageTk,PhotoImage(Image.open(file))

    plabel = tkinter.Label(image = back_pic)
    plabel.configure(image=back_pic)
    plabel.image = back_pic

    pic_label = Label(root, image = back_pic, height = 450, width = 500)
    pic_label.place(x = 0, y = 0)
    pic_label.lower()
    root.attributes("-transparent")

mybutton = Button(root, text = "Play Song", font=("Comic Sans MS", 32), command = play)
mybutton.pack(pady=20)
stop_button = Button(root, text="Stop", command=stop)
stop_button.pack(pady=20)
#backgroung image button
bButton = Button(root, text = "Background", command = add_pic)
bButton.pack(pady = 20)

root.mainloop()
#root.blit(background_image, (0, 0))
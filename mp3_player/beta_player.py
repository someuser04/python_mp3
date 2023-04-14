from tkinter import *
import pygame
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

mybutton = Button(root, text = "Play Song", font=("Comic Sans MS", 32), command = play)
mybutton.pack(pady=20)
stop_button = Button(root, text="Stop", command=stop)
stop_button.pack(pady=20)

root.mainloop()
#root.blit(background_image, (0, 0))
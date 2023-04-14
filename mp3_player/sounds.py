from tkinter import *
import pygame
root = Tk()
root.title('Mp3 player')
root.iconbitmap()
root.geometry("500x400")

pygame.mixer.init()

song_box = Listbox(root, bg="black", fg="green", width=60)
song_box.pack(pady=20)

back_btn_img = PhotoImage(file='back_button.png')
foward_btn_img = PhotoImage(file='foward_button.png')
play_btn_img = PhotoImage(file='play_button.jpg')
pause_btn_img = PhotoImage(file='pause_button.png')
stop_btn_img = PhotoImage(file='stop_button.png')

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
foward_button = Button(controls_frame, image=foward_btn_img, borderwidth=0)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0)
pause_buton = Button(controls_frame, image=pause_btn_img, borderwidth=0)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0)

back_button.grid(row=0, column=0)
foward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_buton.grid(row=0, column=3)
stop_button.grid(row=0, column=4)

root.mainloop() 
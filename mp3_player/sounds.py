from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as tkk
import os
from pathlib import Path
import random
root = Tk()     
root.title('Python Player')
root.iconbitmap()
root.geometry("500x450")
rgb = ["#" +''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
root.configure(background=rgb)
pygame.mixer.init()

def add_tracks():
    current_dir = os.getcwd()
    songs = filedialog.askopenfilenames(initialdir='audio', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))

    for song_file in songs:
        print(song_file)
        #song = song_file.replace('audio', "")
        #song = song.replace(".mp3", "")
        song_list.insert(END, song_file)

def play():
    song = song_list.get(ACTIVE)
    song = f'{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
   

def stop():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)

    status.config(text='')
global paused
paused = False
def pause(is_paused):
    global paused
    paused = is_paused
    if paused == True:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True
        
def foward_song():
    next_song = song_list.curselection()
    next_song = next_song[0] + 1 
    song = song_list.get(next_song)
    song = f'{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_list.selection_clear(0, END)

    song_list.activate(next_song)


    song_list.selection_set(next_song, last=None)
def prev_song():
    next_song = song_list.curselection()
    next_song = next_song[0] - 1 
    song = song_list.get(next_song)
    song = f'{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_list.selection_clear(0, END)

    song_list.activate(next_song)


    song_list.selection_set(next_song, last=None)

def delete_song():
    song_list.delete(ANCHOR)
    pygame.mixer.music.stop()

def clear_track():
    song_list.delete(0,END)
    pygame.mixer.music.stop()



# Create Volume Function
def volume(x):
     pygame.mixer.music.set_volume(1-volume_slider.get())
     current_volume = pygame.mixer.music.get_volume()
     slider_label.config(text=int((current_volume)*100))

# Create Master Frame
master_frame = Frame(root, bg="gray")
master_frame.pack(pady=20, padx=(30,0))

song_list = Listbox(master_frame, bg = "gray", fg="white", width=60, selectbackground="white", selectforeground="black")
song_list.grid(row=1, column=0, columnspan = 2)



back_button_img = PhotoImage(file=('static/11.png'))
foward_button_img = PhotoImage(file=('static/8.png'))
play_button_img = PhotoImage(file=('static/7.png'))
pause_button_img= PhotoImage(file=('static/10.png'))
stop_button_img= PhotoImage(file=('static/6.png'))


controls_frame = Frame(root)
controls_frame.pack()

# Create Volume Label Frame
volume_frame = LabelFrame(master_frame, text="Volume", bg="gray")
volume_frame.grid(row=1, column=3, padx=(0,0))


back_button = Button(controls_frame, image=back_button_img, borderwidth=0,command=prev_song)
foward_button = Button(controls_frame, image=foward_button_img, borderwidth=0,command=foward_song)
play_button = Button(controls_frame, image=play_button_img, borderwidth=0,command=play)
pause_button = Button(controls_frame, image=pause_button_img, borderwidth=0,command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_button_img, borderwidth=0,command=stop)

back_button.grid(row=0, column=0, padx=10)
foward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

menu = Menu(root)
root.config(menu=menu)

add_song_menu = Menu(menu)
menu.add_cascade(label="Add Songs", menu=add_song_menu)

add_song_menu.add_command(label="Add songs to playlist", command=add_tracks)

remove_song_menu = Menu(menu)
menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a Song from playlist", command = delete_song)
remove_song_menu.add_command(label="Clear Playlist", command = clear_track)

# Create Volume Slider
volume_slider = tkk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=0, command=volume, length = 111)
volume_slider.pack(pady=(10, 4))

# Create Current Volume Label
slider_label = Label(volume_frame, text="100", bg="gray")
slider_label.pack()


status = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status.pack(fil=X, side=BOTTOM, ipady=2)




root.mainloop()


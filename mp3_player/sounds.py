from tkinter import *
import pygame
from tkinter import filedialog
root = Tk()
root.title('Mp3 player')
root.iconbitmap()
root.geometry("500x400")

pygame.mixer.init()

def add_track():
    song = filedialog.askopenfile(initialdir='audio/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))
    #song = song.replace("C:/Users/juant/Desktop/python_mp3/mp3_player/audio/", "")
    #song = song.replace(".mp3", "")
    song_list.insert(END, song)
def play():
    song = song_list.get(ACTIVE)
    song = f'audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)

song_list = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_list.pack(pady=20)

#back_button = PhotoImage(file='button_back50.png')
#foward_button = PhotoImage(file='mp3_player/photos/button_forward50.png')
#play_button = PhotoImage(file='mp3_player/photos/play50.png')
#pause_button = PhotoImage(file='mp3_player/photos/pause50.png')
#stop_button = PhotoImage(file='mp3_player/photos/stop50.png')


controls_frame = Frame(root)
controls_frame.pack()

#back_button = Button(controls_frame, image=back_button, borderwidth=0)
#foward_button = Button(controls_frame, image=foward_button, borderwidth=0)
#play_button = Button(controls_frame, image=play_button, borderwidth=0)
#pause_button = Button(controls_frame, image=pause_button, borderwidth=0)
#stop_button = Button(controls_frame, image=stop_button, borderwidth=0)

#back_button.grid(row=0, column=0, padx=10)
#foward_button.grid(row=0, column=1, padx=10)
#play_button.grid(row=0, column=2, padx=10)
#pause_button.grid(row=0, column=3, padx=10)
#stop_button.grid(row=0, column=4, padx=10)

menu = Menu(root)
root.config(menu=menu)

add_song_menu = Menu(menu)
menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add song to playlist", command=add_track)
root.mainloop()

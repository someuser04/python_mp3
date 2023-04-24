from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as tkk
root = Tk()
root.title('Mp3 player')
root.iconbitmap()
root.geometry("500x450")

pygame.mixer.init()

def add_track():
    song = filedialog.askopenfile(initialdir='audio/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))
    #song = song.replace("C:/Users/juant/Desktop/python_mp3/mp3_player/audio/", "")
    #song = song.replace(".mp3", "")
    song_list.insert(END, song)
def add_tracks():
    songs = filedialog.askopenfile(initialdir='audio/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))

    for song in songs:
        song = song.replace("C:/Users/juant/Desktop/python_mp3/mp3_player/audio/", "")
        song = song.replace(".mp3", "")
        song_list.insert(END, song)
def play():
    song = song_list.get(ACTIVE)
    song = f'audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    time()

    slider_position = int(song_l)
    slider.config(to=slider_position, value=0)

def stop():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)

    status.config(text='')

def foward_song():
    next_song = song_list.curselection()
    next_song = next_song[0] + 1 
    song = song_list.get(next_song)
    song = f'audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_list.selection_clear(0, END)

    song_list.activate(next_song)


    song_list.selection_set(next_song, last=None)
def prev_song():
    next_song = song_list.curselection()
    next_song = next_song[0] - 1 
    song = song_list.get(next_song)
    song = f'audio/{song}.mp3'

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

def time():
    current_time = pygame.mixer.music.get_pos() / 1000
    
    converted_current_time = time.strftime('%H:%M:%S', time.gmtime(current_time))
    status.config(text=f'Time Elapsed:{converted_current_time} of {converted_song_l}  ')
    slider.config(value=int(current_time))
    #current_song = song_list.curselection()
    song = song_list.get(ACTIVE)
    song = f'audio/{song}.mp3'

    song_mute = MP3(song)
    global song_l

    song_l = song_mute.info.length
    converted_song_l = time.strftime('%H:%M:%S', time.gmtime(song_l))
    
    status.after(1000, time)
global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def slide(x):
    slider_label.config(text=f'{int(slider.get())} of {int(song_l)}')


song_list = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_list.pack(pady=20)

back_button = PhotoImage(file='C:/Users/juant/Desktop/python_mp3/mp3_player/photos/button_back50.png')
foward_button = PhotoImage(file='C:/Users/juant/Desktop/python_mp3/mp3_player/photos/button_forward50.png')
play_button = PhotoImage(file='C:/Users/juant/Desktop/python_mp3/mp3_player/photos/play50.png')
pause_button = PhotoImage(file='C:/Users/juant/Desktop/python_mp3/mp3_player/photos/pause50.png')
stop_button = PhotoImage(file='C:/Users/juant/Desktop/python_mp3/mp3_player/photos/stop50.png')


controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_button, borderwidth=0)
foward_button = Button(controls_frame, image=foward_button, borderwidth=0)
play_button = Button(controls_frame, image=play_button, borderwidth=0)
pause_button = Button(controls_frame, image=pause_button, borderwidth=0)
stop_button = Button(controls_frame, image=stop_button, borderwidth=0)

back_button.grid(row=0, column=0, padx=10)
foward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

menu = Menu(root)
root.config(menu=menu)

add_song_menu = Menu(menu)
menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add song to playlist", command=add_track)

add_song_menu.add_command(label="Add songs to playlist", command=add_tracks)

remove_song_menu = Menu(menu)
menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a Song from playlist", command = delete_song)
remove_song_menu.add_command(label="Clear Playlist", command = clear_track)

status = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status.pack(fil=X, side=BOTTOM, ipady=2)

slider = tkk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
slider.pack(pady=30)

slider_label = Label(root, text="0")
slider_label.pack(pady=10)

root.mainloop()

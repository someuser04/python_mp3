from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as tkk

root = Tk()     
root.title('Mp3 player')
root.iconbitmap("C:/Users/evale/OneDrive/Documents/musicprog/images/Wwalczyszyn-Android-Style-Honeycomb-Music.ico")
root.geometry("500x450")

pygame.mixer.init()

def add_track():
    song = filedialog.askopenfile(initialdir='audio/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))
    song = song.name.replace("C:/Users/evale/OneDrive/Documents/musicprog/audio/", "")
    song = song.replace(".mp3", "")
    song_list.insert(END, song)

def add_tracks():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))

    for song_file in songs:
        song = song_file.replace("C:/Users/evale/OneDrive/Documents/musicprog/audio/", "")
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
    next_song = song_list.curselection
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
    # Get Current Volume
    pygame.mixer.music.load(song_list)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))


# Create Volume Function
def volume(x):
     pygame.mixer.music.set_volume(1-volume_slider.get())
     current_volume = pygame.mixer.music.get_volume()
     slider_label.config(text=int((current_volume)*100))

# Create Master Frame
master_frame = Frame(root, bg="gray")
master_frame.pack(pady=20, padx=(30,0))

song_list = Listbox(master_frame, bg = "black", fg="green", width=60, selectbackground="white", selectforeground="black")
song_list.grid(row=1, column=0, columnspan = 2)

#song_list = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
#song_list.pack(pady=20)

back_button_img = PhotoImage(file='C:/Users/evale/OneDrive/Documents/musicprog/images/back.png')
foward_button_img = PhotoImage(file='C:/Users/evale/OneDrive/Documents/musicprog/images/forward.png')
play_button_img = PhotoImage(file='C:/Users/evale/OneDrive/Documents/musicprog/images/play.png')
pause_button_img= PhotoImage(file='C:/Users/evale/OneDrive/Documents/musicprog/images/pause.png')
stop_button_img= PhotoImage(file='C:/Users/evale/OneDrive/Documents/musicprog/images/stop.png')


controls_frame = Frame(root)
controls_frame.pack()

# Create Volume Label Frame
volume_frame = LabelFrame(master_frame, text="Volume", bg="gray")
volume_frame.grid(row=1, column=3, padx=(0,0))


back_button = Button(controls_frame, image=back_button_img, borderwidth=0)
foward_button = Button(controls_frame, image=foward_button_img, borderwidth=0)
play_button = Button(controls_frame, image=play_button_img, borderwidth=0)
pause_button = Button(controls_frame, image=pause_button_img, borderwidth=0)
stop_button = Button(controls_frame, image=stop_button_img, borderwidth=0)

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

# Create Volume Slider
volume_slider = tkk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=0, command=volume, length = 111)
volume_slider.pack(pady=(10, 4))

# Create Current Volume Label
slider_label = Label(volume_frame, text="100", bg="gray")
slider_label.pack()


status = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status.pack(fil=X, side=BOTTOM, ipady=2)

slider = tkk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
slider.pack(pady=30)

slider_label = Label(root, text="0")
slider_label.pack(pady=10)


root.mainloop()

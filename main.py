import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music PLayer")
canvas.geometry("600x800")
canvas.config(bg="black")

rootpath="C:\\Users\haris\Music"
pattern="*.mp3"

mixer.init()

previmg = tk.PhotoImage(file="D:\python_prgs\musicplayer\prev.png")
stopimg = tk.PhotoImage(file="D:\python_prgs\musicplayer\stop.png")
pauseimg = tk.PhotoImage(file="D:\python_prgs\musicplayer\pause.png")
nextimg = tk.PhotoImage(file="D:\python_prgs\musicplayer\\next.png")
playimg = tk.PhotoImage(file="D:\python_prgs\musicplayer\play.png")

def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath+"\\"+listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear("active")

def play_next():
    next_song=listbox.curselection()
    next_song=next_song[0] + 1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listbox.select_clear(0,"end")
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    next_song=listbox.curselection()
    next_song=next_song[0] - 1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listbox.select_clear(0,"end")
    listbox.activate(next_song)
    listbox.select_set(next_song)

def pause_song():
    if pausebutton["text"] == "pause":
        mixer.music.pause()
        pausebutton["text"]="play"
    else:
        mixer.music.unpause()
        pausebutton["text"]="pause"


listbox=tk.Listbox(canvas,fg="cyan",bg="black",width=100,font=("popins",16))
listbox.pack(padx=15,pady=15)

label=tk.Label(canvas,text="",bg="black",fg="yellow",font=("popins",14))
label.pack(pady=15)

top=tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=5,anchor="center")

prevbutton=tk.Button(canvas,text="prev",image=previmg,bg="black",borderwidth=0,command=play_prev)
prevbutton.pack(pady=15,in_ = top,side = "left")

stopbutton=tk.Button(canvas,text="stop",image=stopimg,bg="black",borderwidth=0,command=stop)
stopbutton.pack(pady=15,in_ = top,side = "left")

playbutton=tk.Button(canvas,text="play",image=playimg,bg="black",borderwidth=0,command=select)
playbutton.pack(pady=15,in_ = top,side = "left")

pausebutton=tk.Button(canvas,text="pause",image=pauseimg,bg="black",borderwidth=0,command=pause_song)
pausebutton.pack(pady=15,in_ = top,side = "left")

nextbutton=tk.Button(canvas,text="next",image=nextimg,bg="black",borderwidth=0,command=play_next)
nextbutton.pack(pady=15,in_ = top,side = "left")

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert("end",filename)

canvas.mainloop()
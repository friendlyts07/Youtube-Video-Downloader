# -*- coding: utf-8 -*-
from pytube import YouTube
import os
from tkinter import *

root = Tk()

root.geometry('1500x900')
root.title(" Video Download from Youtube")
           
Label_1=Label(root,text="Paste Your Youtube Link Here",fg="red", font=("bold",46))
Label_1.place(x=150, y=70)

Label_2=Label(root, text= "This is for Doing activity don't misuse it",fg="red", font=("bold", 30))
Label_2.place(x=180, y=150)

Label_3= Label(root, text= "Hope You all like this Script", font=("bold", 30))
Label_3.place(x=180, y=200)

mylink=StringVar()
pastelink=Entry(root, width=150, textvariable=mylink)
pastelink.place(x=190, y=270)

def downloadvideo():
    x= str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('F:/New folder'):
        os.makedirs('F:/New folder')
    ytvideo.download('F:/New folder') 

Button(root,text="Download Video", width=40,height=2, bg='green',fg="white", command= downloadvideo).place(x=820, y=300)


    

root.mainloop()


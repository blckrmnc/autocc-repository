# A personal project by blckrmnc
# Developed, 2020 (For school portfolio, 2020)

import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk, Image, ImageEnhance
import tkinter.filedialog
import os, os.path
import cv2

root = tk.Tk()
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)

root.title("AutoCC")
root.geometry("600x500")

fbright = tkinter.Frame(root)
fbright.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.1)

fsharp = tkinter.Frame(root)
fsharp.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.1)

fcont = tkinter.Frame(root)
fcont.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

fcolor = tkinter.Frame(root)
fcolor.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.1)

fileLabel = Label()

def select_image():

    root.fileBrowse = tkinter.filedialog.askopenfilename()
    fileLabel.config(text=root.fileBrowse)
    fileLabel.pack()

def enhance_image():

    brightVal = int(brightEnt.get())
    sharpVal = int(sharpEnt.get())
    contVal = int(contEnt.get())
    colorVal = int(colorEnt.get())

    image = ImageEnhance.Brightness(Image.open(root.fileBrowse)).enhance(brightVal)
    image = ImageEnhance.Sharpness(image).enhance(sharpVal)
    image = ImageEnhance.Contrast(image).enhance(contVal)
    image = ImageEnhance.Color(image).enhance(colorVal)

    path = "cc_folder"

    if not os.path.exists(path):
        os.makedirs(path)
    fileName = os.path.basename(root.fileBrowse)
    image.save(os.path.join(path, fileName))

appTitle = Label(root, text="AutoCC", fg='#28527a', font=("Colombo", 40, 'bold'))
appTitle.pack()

appSubtitle = Label(root, text="A project by Max")
appSubtitle.pack(pady=20)

status = Label(root, text="Status: ONLINE", fg='green')
status.pack()

browseBtn = Button(root, text="Select Image", command=select_image)
browseBtn.pack()

brightLabel = Label(fbright, text="Brightness:")
brightLabel.pack(side=LEFT)
brightEnt = Entry(fbright)
brightEnt.insert(0, 1)
brightEnt.pack(side=RIGHT)

sharpLabel = Label(fsharp, text="Sharpness:")
sharpLabel.pack(side=LEFT)
sharpEnt = Entry(fsharp)
sharpEnt.insert(0, 1)
sharpEnt.pack(side=RIGHT)

contLabel = Label(fcont, text="Contrast:")
contLabel.pack(side=LEFT)
contEnt = Entry(fcont)
contEnt.insert(0, 1)
contEnt.pack(side=RIGHT)

colorLabel = Label(fcolor, text="Saturation")
colorLabel.pack(side=LEFT)
colorEnt = Entry(fcolor)
colorEnt.insert(0, 1)
colorEnt.pack(side=RIGHT)

enhanceBtn = Button(root, text="Enhance Image", command=enhance_image)
enhanceBtn.pack(pady=10)

infoLabel = Label(root, text="Settings. (Optimal ranges from 0.5 to 1.5)")
infoLabel.pack()

infoLabel1 = Label(root, text="Enhanced files are saved to cc_folder")
infoLabel1.pack()

#   .__(.)< (MEOW)
#    \___)

root.mainloop()

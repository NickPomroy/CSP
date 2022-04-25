import tkinter as tk
from turtle import onclick
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import json
import config as cfg

def refresh(x):
    pass

# Window section
root = tk.Tk()
root.title('ISS Location')
root.geometry('600x600')

display = tk.Label(root,font=('Arial 18 bold'),fg='red')
display.grid(row=0,column=0)
display.bind('<Button>',refresh)

iss_location = get_iss_location('https://api.open-notify.org/iss-now.json')

root.mainloop()
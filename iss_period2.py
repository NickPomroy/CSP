import tkinter as tk
from turtle import onclick
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import json
import config as cfg

# Window section
root = tk.Tk()
root.title('ISS Location')
root.geometry('600x600')

root.mainloop()
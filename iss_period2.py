from logging import exception
import tkinter as tk
from turtle import onclick
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import json
import config as cfg

def get_iss_location(url:str):
    try:
        iss_request = urlopen(url)
        iss_location = json.loads(iss_request.read())

        print(iss_location)

        longitude = iss_location['iss_position']['longitude']
        latitude = iss_location['iss_position']['latitude']

        return longitude, latitude
    except Exception as e:
        print(e)
        root.quit()

def refresh(x):
    pass



# Window section
root = tk.Tk()
root.title('ISS Location')
root.geometry('600x600')

display = tk.Label(root,font=('Arial 18 bold'),fg='red')
display.grid(row=0,column=0)
display.bind('<Button>',refresh)

iss_location = get_iss_location('http://api.open-notify.org/iss-now.json')

root.mainloop()
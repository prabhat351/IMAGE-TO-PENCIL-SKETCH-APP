#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Function to open and process the image
def process_image():
    file_path = filedialog.askopenfilename()  # Open a file dialog to choose an image
    if file_path:
        img = cv2.imread(file_path, cv2.IMREAD_COLOR)
        if img is None:
            result_label.config(text="Error: Unable to load the image.")
            return
        
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inv = cv2.bitwise_not(grey)
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        invblur = cv2.bitwise_not(blur)
        sketch = cv2.divide(grey, invblur, scale=250.0)
        
        # Convert the result image to PIL format and display it
        sketch_pil = Image.fromarray(sketch)
        sketch_tk = ImageTk.PhotoImage(image=sketch_pil)
        result_label.config(image=sketch_tk)
        result_label.image = sketch_tk

# Create the main application window
app = tk.Tk()
app.title("Image Sketch App")

# Create and configure widgets
load_button = tk.Button(app, text="Load Image", command=process_image)
result_label = tk.Label(app)

# Pack widgets
load_button.pack(pady=10)
result_label.pack()
app.mainloop()


# In[ ]:





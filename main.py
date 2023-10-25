
y = 2


import tkinter as tk
from numpy import negative, arange
from config import *
app = tk.Tk()
app.title("Function")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{size_x}x{size_y}+{(screen_width-size_x)//2}+{(screen_height-size_y)//2}")


canvas = tk.Canvas(app, width=window_width, height=window_height)
canvas.pack()  

def start():
    line_x = canvas.create_line(0, window_height//2, window_width, window_height//2, fill="#000000", width=2)
    line_y = canvas.create_line(window_width//2, 0, window_width//2, window_height, fill="#000000", width=2)
    for i in range(0, window_width, scale_y):
        canvas.create_line(
            i,
            center_y - line_l,
            i ,
            center_y + line_l,
            fill="black",
            width=2
        )

    for i in range(0, window_height, scale_x):
        canvas.create_line(
            center_x - line_l,
            i ,
            center_x + line_l,
            i ,
            fill="black",
            width=2
        )
    
    dot_center = canvas.create_oval(
    center_x - dot_r,
    center_y - dot_r,
    center_x + dot_r,
    center_y + dot_r,
    fill="red"  # You can change the fill color as desired
    )


def function1(y):
    function_list = [] 
    for x in arange(width*-1, width): # clever system for idk what :)
        function_list.extend([x+ width, negative((x **y))+ height])  # Add each point as a separate coordinate
    line = canvas.create_line(*function_list, fill="yellow", width=2)  # Pass the list as arguments

def function2(y):
    function_list = []  # Create an empty list to store the points
    for x in arange(width*-1, width): # clever system for idk what :)
        function_list.extend([x + width, negative(((x/scale_x) **y))*scale_y+ height])  # Add each point as a separate coordinate
        print(x, negative(((x/scale_x) **y))*scale_y+ height)
    line = canvas.create_line(*function_list, fill="red", width=2)  # Pass the list as arguments

    
# Draw a line on the screen
start()

# function1(y)
function2(y)

# Start the Tkinter event loop
app.mainloop()

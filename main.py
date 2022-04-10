#import libraries that are needed to run the program.
from tkinter import *
mainwindow = Tk() #initiates Tkinter
mainwindow.geometry = ("320x240")
canvasarea = Canvas(mainwindow, width=320, height=240)
canvasarea.pack()
canvas_height=320
canvas_width=240

def drawpixel(): #drawing the pixel on the canvas
    canvasarea.create_line(100, 100, 101, 100, fill="#FF0000") #FF0000 is hex code for (255,0,0)
    #The reason why the second X coordinate is 101 is because it makes zero sense if a line is 0 px long.
    #A pixel would only be 1px long, so in this case the length of the "line" is 1px as we made a dot.
    mainwindow.mainloop() #initiates Window

if __name__ == "__main__":
    drawpixel()
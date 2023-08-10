#Tutorial to make a simple digital clock


#import tkinter, using label and TK

#lets us create a small window or screen
from tkinter import Tk
#allows us to put text to our screen
from tkinter import Label

#import time and system that gather us time and store it as a string
import time
import sys


#define a master screen
master = Tk()
#window title
master.title("Digital Clock")

#function that gets time for us and updates label every .2 milisecond
def get_time():
    #time variable, that shows Hours, minutes, seconds and pm or am
    timeVar = time.strftime("%I:%M:%S %p")
    #main of the label, to add text with the time variable
    clock.config(text=timeVar)
    #method that every .2 ms runs this function so it keeps updating
    clock.after(200,get_time)

#create label on our screen, master is where is gonna be placed, font, and backgroundcolor and font color
clock = Label(master, font=("Arial", 100), bg="grey", fg="black")
#puts label in center of screen
clock.pack()

#get time function one last time
get_time()
5
#we need a loop so it keeps running
master.mainloop()
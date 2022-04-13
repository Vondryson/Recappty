from tkinter import *
import tkinter as tk


## Main menu of the app

root= Tk()
root.title("Recappty")
global recepty_lookup_window
global add_recepy_window

def recepy_lookup():
	recepty_lookup_window = Toplevel()
	recepty_lookup_window.geometry("400x400")
	frame_recepty_lookup_window = LabelFrame(recepty_lookup_window)
	frame_recepty_lookup_window.grid()

	nadpis = Label(recepty_lookup_window, text="Recepy lookup").grid(row=0, columnspan=2, column=0)
	




def add_recepy():
	add_recepy_window = Toplevel()




## main menu 

title = Label(root, text = "Recappty", font="Helvetica").grid(row = 0, columnspan = 2)
frame1 = LabelFrame(root,padx=5,pady=5)
frame1.grid(padx=10,pady=10, column = 0, row = 1 )
frame2 = LabelFrame(root,padx=5,pady=5)
frame2.grid(padx=10,pady=10, column= 1, row = 1)
frame3 = LabelFrame(root,padx=5,pady=5)
frame3.grid(padx=10,pady=10, column = 0, row = 2)
frame4 = LabelFrame(root,padx=5,pady=5)
frame4.grid(padx=10,pady=10, column = 1, row = 2)

b1 = Button(frame1, text="Možnost 1", height= 10,  width = 20, padx = 5, pady = 5, command=recepy_lookup)
b1.pack()
b2 = Button(frame2, text="Možnost 2", height= 10,  width = 20, padx = 5, pady = 5)
b2.pack()
b3 = Button(frame3, text="Možnost 3", height= 10,  width = 20, padx = 5, pady = 5)
b3.pack()
b4 = Button(frame4, text="Možnost 4", height= 10,  width = 20, padx = 5, pady = 5)
b4.pack()








root.mainloop()
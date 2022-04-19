from tkinter import *
import tkinter as tk
import sqlite3



## Main menu of the app


root= Tk()
root.title("Recappty")
global recepty_lookup_window
global add_recipe_window
name_var=StringVar()
ingre_var=StringVar()
steps_var=StringVar()
category_var=StringVar()
time_var=IntVar()





conn = sqlite3.connect("Recappty.db")
c = conn.cursor()

try:

	c.execute("""CREATE TABLE Recappty (
		name text, 
		ingre text, 
		steps text,
		category text, 
		aprrox_time integer
		
		)""")
except:
	pass

conn.close()

def recipe_lookup():
	recepty_lookup_window = Toplevel()
	recepty_lookup_window.geometry("400x400")
	frame_recepty_lookup_window = LabelFrame(recepty_lookup_window)
	frame_recepty_lookup_window.grid()

	nadpis = Label(recepty_lookup_window, text="Recipe lookup").grid(row=0, columnspan=2, column=0)
	ID_entry_label=Label(recepty_lookup_window, text="ID:").grid(row=1,column=0)
	ID_entry = Entry(recepty_lookup_window, width = 50).grid(row=1, column=1,padx=5)

	ingre_entry_label=Label(recepty_lookup_window, text="Ingre:").grid(row=2,column=0)
	ingre_entry = Entry(recepty_lookup_window, width = 50).grid(row=2, column=1,padx=5,pady=5)

	category_entry_label=Label(recepty_lookup_window, text="Category:").grid(row=3,column=0)
	category_entry = Entry(recepty_lookup_window, width = 50).grid(row=3, column=1,padx=5,pady=5)


	b_lookup = Button(recepty_lookup_window, text="Find recipe", width=50).grid(row=4, columnspan=2, pady=5, padx = 5)

def recipe_add():
	recepty_add_window = Toplevel()
	recepty_add_window.geometry("400x400")
	frame_recepty_add_window = LabelFrame(recepty_add_window)
	frame_recepty_add_window.grid()

	nadpis = Label(recepty_add_window, text="Add Recipe").grid(row=0, columnspan=2, column=0)
	name_entry_label=Label(recepty_add_window, text="Name:").grid(row=1,column=0)
	name_entry = Entry(recepty_add_window, width = 50, textvariable=name_var).grid(row=1, column=1,padx=5)

	ingre_entry_label=Label(recepty_add_window, text="Ingre:").grid(row=2,column=0)
	ingre_entry = Entry(recepty_add_window, width = 50, textvariable=ingre_var).grid(row=2, column=1,padx=5,pady=5)

	steps_entry_label=Label(recepty_add_window, text="Steps:").grid(row=3,column=0)
	steps_entry = Entry(recepty_add_window, width = 50, textvariable=steps_var).grid(row=3, column=1,padx=5,pady=5)

	category_entry_label=Label(recepty_add_window, text="Category:").grid(row=4,column=0)
	category_entry = Entry(recepty_add_window, width = 50, textvariable=category_var).grid(row=4, column=1,padx=5,pady=5)

	time_entry_label=Label(recepty_add_window, text="Time:").grid(row=5,column=0)
	time_entry = Entry(recepty_add_window, width = 50, textvariable=time_var).grid(row=5, column=1,padx=5,pady=5)


	b_add = Button(recepty_add_window, text="Add recipe", width=50, command=add_recipe).grid(row=6, columnspan=2, pady=5, padx = 5)

	warning_notes_label = Label(recepty_add_window, text="Please note!", fg="red", font=("Arial",15)).grid(row=7,columnspan=2,pady=7)

	ingre_notes_label = Label(recepty_add_window, text="Separate each ingrediens with comma").grid(row=8, columnspan=2, pady=5)
	steps_notes_label = Label(recepty_add_window, text="Separate each step with slash /").grid(row=9, columnspan=2, pady=5)













def add_recipe():
	conn = sqlite3.connect("Recappty.db")
	c = conn.cursor()
	c.execute("INSERT INTO Recappty VALUES (:name, :ingre, :steps, :category, :aprrox_time)",
		{
		"name": name_var.get(),
		"ingre": ingre_var.get(),
		"steps": steps_var.get(),
		"category": category_var.get(),
		"aprrox_time":time_var.get()

		}

		)



	conn.commit()
	conn.close()

	#name_entry.delete(0,END)
	#ingre_entry.delete(0,END)
	#steps_entry.delete(0,END)
	#category_entry.delete(0,END)
	#time_entry.delete(0,END)




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

b1 = Button(frame1, text="Možnost 1", height= 10,  width = 20, padx = 5, pady = 5, command=recipe_lookup)
b1.pack()
b2 = Button(frame2, text="Možnost 2", height= 10,  width = 20, padx = 5, pady = 5, command=recipe_add)
b2.pack()
b3 = Button(frame3, text="Možnost 3", height= 10,  width = 20, padx = 5, pady = 5)
b3.pack()
b4 = Button(frame4, text="Možnost 4", height= 10,  width = 20, padx = 5, pady = 5)
b4.pack()








root.mainloop()
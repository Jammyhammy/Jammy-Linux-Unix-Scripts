#!/usr/bin/python

from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import tkinter

classes = ['CMPS260-001','CMPS260-002','CMPS261-001','CMPS327-001','CMPS450-001','CMPS499-002']
profs = ['Dr.Radle', 'Dr.Etheridge', 'Dr.Kumar', 'Mr.Ducrest']
courseprofs = { 'CMPS260-001': 'Dr.Etheridge',
	        'CMPS260-002': 'Mr.Ducrest',
		'CMPS261-001': 'Dr.Etheridge',
		'CMPS327-001': 'Dr.Etheridge',
		'CMPS455-001': 'Dr.Kumar',
		'CMPS499-002': 'Dr.Radle'
}

class main(tkinter.Tk):
	def __init__(self, *args, **kwargs):
		tkinter.Tk.__init__(self, *args, **kwargs)
		
		container = tkinter.Frame(self)
		container.pack(side="top", fill="both", expand=True)

		
		self.frames = {}
		for F in (mainMenu, listClassFrame, listProfFrame):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
			self.show_frame(mainMenu)

	def show_frame(self, c):
		frame = self.frames[c]
		frame.tkraise()
	
class mainMenu(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)

		profLabel = tkinter.Label(self, text="Name").grid(row=0, column=0, sticky=W)
    		nameVar = StringVar()
    		name = Entry(self, textvariable=nameVar)
    		name.grid(row=0, column=1, sticky=N)

    		courseLabel = tkinter.Label(self, text="Phone").grid(row=1, column=0, sticky=W)
    		phoneVar= StringVar()
    		phone= Entry(self, textvariable=phoneVar)
    		phone.grid(row=1, column=1, sticky=N)


		listClassButton = tkinter.Button(self, text="List of classes", width = 20, command=lambda: controller.show_frame(listClassFrame))
		listClassButton.pack(side = LEFT)
		listProfsButton = tkinter.Button(self, text="List of professors", width = 20, command=lambda: controller.show_frame(listProfFrame))
		listProfsButton.pack(side = LEFT)
		APButton = tkinter.Button(self, text="Add a professor", width = 20, command=addProf)
		APButton.pack(side = LEFT)
		ACButton = tkinter.Button(self, text="Add a class", width = 20, command=addClass)
		ACButton.pack(side = LEFT)
		RPButton = tkinter.Button(self, text="Remove a professor", width = 20, command=remProf)
		RPButton.pack(side = LEFT)
		RCButton = tkinter.Button(self, text="Remove a class", width = 20, command=remClass)
		RCButton.pack(side = LEFT)

		clabel = tkinter.Label(self, text = "List of Classes")
		clabel.pack(side="left", fill="x", pady=1)
		classListBox = Listbox(self)	
		i = 0
		for course in classes:
			classListBox.insert(i,course)
			i = i + 1
		classListBox.pack()

		profListBox = Listbox(self)
		j = 0
		for prof in profs:
			profListBox.insert(i,prof)
			j = j + 1
		profListBox.pack()

		label1 = tkinter.Label( self, text = "test")
		e1 = Entry(self, bd = 5)
		
		def addProf():
		def remProf():
		def addClass():
		def remClass():
		
		submit = Button(self, text ="Submit", command = gettest)

		label1.pack()
		e1.pack()
		submit.pack(side = BOTTOM)

		label = tkinter.Label(self, text="Menu")
		label.pack(side='top', pady=1)

			
class listClassFrame(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = tkinter.Label(self, text = "List of Classes")
		label.pack(side="top", fill="x", pady=1)

		classListBox = Listbox(self)	
		i = 0
		for professor in classes:
			for course in professor:
				classListBox.insert(i,course)
				i = i + 1
		classListBox.pack()
		
		button = tkinter.Button(self, text="Return", command=lambda: controller.show_frame(mainMenu))
		button.pack()
class listProfFrame(tkinter.Frame):
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		label = tkinter.Label(self, text = "List of Professors")
		label.pack(side="top", fill="x", pady=1)
		
		profListBox = Listbox(self)
		
		i = 0
		for prof in profs:
			profListBox.insert(i,prof)
			i = i + 1

		profListBox.pack()

		label1 = tkinter.Label( self, text = "test")
		e1 = Entry(self, bd = 5)
		
		def gettest():
			e1.get()
		
		submit = Button(self, text ="Submit", command = gettest)

		label1.pack()
		e1.pack()
		submit.pack(side = BOTTOM)		

		
		button = tkinter.Button(self, text="Return", command = lambda: controller.show_frame(mainMenu))
		button.pack()
		
if __name__ == "__main__":
	app = main()
	app.mainloop()

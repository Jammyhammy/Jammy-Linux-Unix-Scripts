#!/usr/bin/python3
# Adil Khokhar
# CLID: axk9375
# CMPS 499 python assignment designed to work on python 3.2.3

#
# USER GUIDE:
#
#
#
#
#
#
#
#
#

# Import tkinter

from tkinter import *
from tkinter import messagebox
import tkinter.messagebox

class CourseApp():
	
# Initializes the course list app.
	
	def __init__(self, parent):
		
		self.courselist = {}
		self.classes = []
		self.profs = []
		
		entryFrame = Frame(parent)
		entryFrame.pack()
		entlabel = Label(entryFrame, text = "Professor & Course Entry")
		entlabel.pack()
		entlabel.grid(row=1, column=1)
		self.profField = Entry(entryFrame, text = "Professor", width=30)
		self.profField.insert(0, "Dr. Radle")
		self.profField.pack()
		self.profField.grid(row=2, column=1)
		self.courseField = Entry(entryFrame, text = "course", width=30)
		self.courseField.insert(0, "CMPS499-001")
		self.courseField.pack()
		self.courseField.grid(row=3, column=1)
		

		buttonFrame = Frame(parent)
		buttonFrame.pack()

#Add in buttons for adding/removing professors, classes, and assignments.

		paddbutt = Button(buttonFrame, text="Add Professor", width = 30, command = self.addProf)
		paddbutt.pack(side = BOTTOM)
		caddbutt = Button(buttonFrame, text="Add Class", width = 30, command = self.addClass)
		caddbutt.pack(side = BOTTOM)

		prembutt = Button(buttonFrame, text="Remove Professor", width = 30, command = self.remProf)
		prembutt.pack(side = BOTTOM)
		crembutt = Button(buttonFrame, text="Remove Class", width = 30, command = self.remClass)
		crembutt.pack(side = BOTTOM)


		pclabutt = Button(buttonFrame, text="Add Assignment", width = 30, command = self.addEntry)
		pclabutt.pack(side = BOTTOM)
		pclrbutt = Button(buttonFrame, text="Remove Assignment", width = 30, command = self.remEntry)
		pclrbutt.pack(side = BOTTOM)

		listFrame = Frame(parent)
		listFrame.pack()

		clabel = Label(listFrame, text = "Classes                       Professors")
		clabel.pack(side= TOP)

		self.classListBox = Listbox(listFrame)	
		self.classListBox.pack( side = LEFT )

# Create and label the listboxes for classes, professors, and assignments

		self.profListBox = Listbox(listFrame)
		self.profListBox.pack( side = LEFT )

		listFrame2 = Frame(parent)
		listFrame2.pack()
		clabel2 = Label(listFrame2, text = "Assignments")
		clabel2.pack(  )
		
		self.clabel3 = Label(listFrame2, text = "")
		self.clabel3.pack(  )

#		Originally used a ListBox widget implementation for the assignments.
#		Found generating labels from the dictionary easier to work with.
#		self.pclListBox = Listbox(listFrame2, width = 40)
#		for prof,course in courselist :
#			pclListBox.insert(END, prof, course)
#		self.pclListBox.pack( side = BOTTOM )
	




	
#	Coursebook Functions:
#	-----------------------------------------------------------------------
#	addProf:	Adds a professor from the Professor Entry Widget to the 
#			professor ListBox.
#	-----------------------------------------------------------------------

	def addProf(self):
		profadd = self.profField.get()
		self.profListBox.insert(END, (profadd))
		self.syncEntries

#	-----------------------------------------------------------------------
#	remProf:	Removes selected professor in the professor ListBox.
#			TODO: Remove all classes professor is teaching from
#			the courselist dictionary.
#	-----------------------------------------------------------------------

	def remProf(self):
		profname = self.profListBox.get(ACTIVE)
		self.profListBox.delete(ANCHOR)
		self.syncEntries

#	-----------------------------------------------------------------------
#	addProf:	Adds a professor from the Professor Entry Widget to the 
#			professor ListBox.
#	-----------------------------------------------------------------------

	def addClass(self):
		classadd = self.courseField.get()
		self.classListBox.insert(END, (classadd))
		self.syncEntries

#	-----------------------------------------------------------------------
#	remProf:	Removes selected professor in the professor ListBox.
#			TODO: Remove all classes professor is teaching from
#			the courselist dictionary.
#	-----------------------------------------------------------------------

	def remClass(self):
		classname = self.classListBox.get(ACTIVE)
		self.remEntry
		self.classListBox.delete(ANCHOR)
		self.syncEntries

#	-----------------------------------------------------------------------
#	addProf:	Adds a professor from the Professor Entry Widget to the 
#			professor ListBox.
#	-----------------------------------------------------------------------

	def addEntry(self):
		profname = self.profListBox.get(ACTIVE)
		classadd = self.classListBox.get(ACTIVE)
		self.courselist[classadd] = profname
		self.clabel3['text'] = '\n'.join('{} {}'.format(k, d) for k, d in self.courselist.items())
		self.clabel3.pack()
		self.syncEntries	

#	-----------------------------------------------------------------------
#	remProf:	Removes selected professor in the professor ListBox.
#			TODO: Remove all classes professor is teaching from
#			the courselist dictionary.
#	-----------------------------------------------------------------------

	def remEntry(self):

		clwin = Toplevel()
		clwin.wm_title("Remove Assignment Entry")
		remFrame = Frame(clwin)
		remFrame.pack()

		cllab = Label(clwin, text="Select the class to remove it as an assignment.")
		cllab.pack()

		self.remListBox = Listbox(remFrame)
		testclass = self.classListBox.get(0,END)
		for courses in testclass:
			self.remListBox.insert(END, courses)
		self.remListBox.pack( side = BOTTOM )
		rembutt = Button(remFrame, text="Remove Assignment", width = 30, command = self.remEntryAct)
		rembutt.pack(side = BOTTOM)

#	-----------------------------------------------------------------------
#	remProf:	Removes selected professor in the professor ListBox.
#			TODO: Remove all classes professor is teaching from
#			the courselist dictionary.
#	-----------------------------------------------------------------------
	
	def remEntryAct(self):
		courserem = self.remListBox.get(ACTIVE)
		self.courselist.pop(courserem, None)
		self.remListBox.delete(ANCHOR)
		self.clabel3['text'] = '\n'.join('{} {}'.format(k, d) for k, d in self.courselist.items())
		self.clabel3.pack()
		self.syncEntries		

#	-----------------------------------------------------------------------
#	remProf:	Removes selected professor in the professor ListBox.
#			TODO: Remove all classes professor is teaching from
#			the courselist dictionary.
#	-----------------------------------------------------------------------

	def syncEntries(self):
		self.profs = self.profListBox.get(0,END)
		self.classes = self.classListBox.get(0,END)

## TODO: Define a sync method that will update from the actual dict and lists to stay consistent.
	
	def quit(self):
		sys.exit()

## Initialize tkinter GUI window and run the application.

root = Tk()
root.title('Course Book')

top = CourseApp(root)
root.mainloop()

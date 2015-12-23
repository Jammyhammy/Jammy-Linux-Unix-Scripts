#!/usr/bin/python3
# Adil Khokhar
# CLID: axk9375
# CMPS 499 python assignment

# Import tkinter

from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import tkinter


# Predefined data of classes and professors.

classes = ['CMPS260-001','CMPS260-002','CMPS261-001','CMPS327-001','CMPS450-001','CMPS499-002']
profs = ['Dr.Radle', 'Dr.Etheridge', 'Dr.Kumar', 'Mr.Ducrest']
courselist = {}
courselist2 = [
	['CMPS260-001', 'Dr.Etheridge'],
	['CMPS260-001', 'Mr.Ducrest'],
	['CMPS261-001', 'Dr.Etheridge'],
]

# Create root window and the frames

root = Tk()
frame = Frame(root)
frame.pack()
frame2 = Frame(root)
frame2.pack( side = BOTTOM )
framelist = Frame(root)
framelist.pack( side = BOTTOM )
frame3 = Frame(root)
frame3.pack( side = BOTTOM )

# Add in entries for user to type in name of professor and course name.

entlabel = Label(frame, text = "Professor & Course Entry")
entlabel.pack()
entlabel.grid(row=1)

profField = Entry(frame, text = "professor", width=30)
profField.insert(0, "ProfName")
profField.pack()
profField.grid(row=2)

courseField = Entry(frame, text = "course", width=30)
courseField.insert(0, "CMPS499-001")
courseField.pack()
courseField.grid(row=3)

# Create and label the listboxes for classes, professors, and assignments

clabel = Label(framelist, text = "Classes                       Professors                        Assignments")
clabel.pack(side= TOP)

classListBox = Listbox(framelist)	
i = 0
for course in classes:
	classListBox.insert(i,course)
	i = i + 1
classListBox.pack( side = LEFT )


profListBox = Listbox(framelist)
j = 0
for prof in profs:
	profListBox.insert(i,prof)
	j = j + 1
profListBox.pack( side = LEFT )

# Dictionary does not work.

#longest = 20
#pclListBox = Listbox(framelist)
#for key,value in courselist.items():
#	entry = '{}: {}'.format(key, (''.join(value)))
#	longest = max(longest, len(entry))
#	pclListBox.insert(END, entry)
#pclListBox.config(width=longest)  
#pclListBox.pack( side = LEFT )

# Just use a list.

pclListBox = Listbox(framelist)
for prof,course in courselist2 :
	pclListBox.insert(END, prof, course)
pclListBox.pack( side = LEFT )

# Function definitions for adding, removing, professors and classes, and assignments.

def addProf():
	profadd = profField.get()
	profListBox.insert(END, (profadd))
	profs.append(profadd)
	
def remProf():
	profname = profListBox.get(ACTIVE)
	profListBox.delete(ANCHOR)
	
def addClass():
	classadd = courseField.get()
	classListBox.insert(END, (classadd))
	classes.append(classadd)
	
def remClass():
	classname = classListBox.get(ACTIVE)
	classListBox.delete(ANCHOR)

def addEntry():
	#An actual assignment manager doesn't work.
	#toplevel = Toplevel()
	#toplevel.title('Manage Assignments')
	#toplevel.focus_set()
	pclListBox.insert(END, classListBox.get(ACTIVE), profListBox.get(ACTIVE))
	courselist2.append([classListBox.get(ACTIVE), profListBox.get(ACTIVE)])

def remEntry():
	pclListBox.delete(ANCHOR)

#Add in buttons for adding/removing professors, classes, and assignments.

paddbutt = Button(frame2, text="Add Professor", width = 30, command = addProf)
paddbutt.pack(side = BOTTOM)
paddbutt.grid(row=1)
caddbutt = Button(frame2, text="Add Class", width = 30, command = addClass)
caddbutt.pack(side = BOTTOM)
caddbutt.grid(row=2)

prembutt = Button(frame2, text="Remove Professor", width = 30, command = remProf)
prembutt.pack(side = BOTTOM)
prembutt.grid(row=3)
crembutt = Button(frame2, text="Remove Class", width = 30, command = remClass)
crembutt.pack(side = BOTTOM)
crembutt.grid(row=4)


pclabutt = Button(frame2, text="Add Assignment", width = 30, command = addEntry)
pclabutt.pack(side = BOTTOM)
pclabutt.grid(row=5)
pclrbutt = Button(frame2, text="Remove Assignment", width = 30, command = remEntry)
pclrbutt.pack(side = BOTTOM)
pclrbutt.grid(row=6)

pcllabel = Label(frame3, text = "For assignments, select a professor and course (the highlighting will disappear but this is fine)")
pcllabel.pack(side= BOTTOM)
pcllabel.grid(row=7)


#Main loop for the window.

root.mainloop()

#!/usr/bin/python

import Tkinter
import os

from Tkinter import *

top = Tkinter.Tk()
top.title("AXEL Download manager GUI")



L1 = Label(top, text="Paste the download link:")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5,width=50)

E1.pack(side = LEFT)



def start():
   url = E1.get()
   os.system("axel %s" % url )
   
B = Tkinter.Button(top, text ="Download now!", command=start)


B.pack()

top.mainloop()


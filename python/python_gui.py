#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text='hell', command=self.hell)
        self.quitButton.pack()

    def hell(self):
        name = self.nameInput.get() or 'word'
        messagebox.showinfo('Message', 'Hello %s' % name)

app = Application()
app.master.title('hell word')
app.mainloop()

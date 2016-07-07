#!/usr/bin/env python

from Tkinter import *
import tkMessageBox
from ScrolledText import ScrolledText
import random, string
import shuffle

class GuiShuffler(shuffle.Shuffler):
    def __init__(self):
        shuffle.Shuffler.__init__(self, 20, 10, 2)

        self.frmMain = Tk()
        self.blockStr = StringVar()
        self.blockSizeStr = StringVar()
        self.groupStr = StringVar()
        self.results = ScrolledText(self.frmMain)

        self.blockStr.set(str(self.blocks))
        self.blockSizeStr.set(str(self.blockSize))
        self.groupStr.set(str(self.groups))

        Label(self.frmMain, text="Blocks").grid(row=0, sticky=E)
        blockEntry = Entry(self.frmMain, textvariable=self.blockStr)
        blockEntry.grid(column=1, row=0)

        Label(self.frmMain, text="Block Size").grid(row=1, sticky=E)
        blockSizeEntry = Entry(self.frmMain, textvariable=self.blockSizeStr)
        blockSizeEntry.grid(column=1, row=1)

        Label(self.frmMain, text="Groups").grid(row=2, sticky=E)
        groupEntry = Entry(self.frmMain, textvariable=self.groupStr)
        groupEntry.grid(column=1, row=2)

        self.results.grid(columnspan=2, row=3, sticky=W+E)

        genBtn = Button(self.frmMain, text="Generate", command=self.generate, anchor=SE)
        genBtn.grid(columnspan=2, row=4, sticky=S)

    def generate(self):
        try:
            self.blocks = int(self.blockStr.get())
            self.blockSize = int(self.blockSizeStr.get())
            self.groups = int(self.groupStr.get())
        except ValueError:
            tkMessageBox.showwarning("Not a Number", "All values must be numbers.\n")
            return

        if not self.is_valid_group_size():
            tkMessageBox.showwarning("Group Size", "Block Size must be evenly divisible by groups to get an even grouping.\n")
        else:
            self.results.delete(1.0, END)       # clear previous entries
            self.print_results(self.results)

    def print_results(self, results):
        for i in  range(self.blocks):
            results.insert(END, ' '.join([str(i) for i in self.shuffle()]))
            results.insert(END, "\n")

    def run(self):
        self.frmMain.mainloop()

if __name__ == "__main__":
    g = GuiShuffler()
    g.run()

#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
import math
import re


class TocEditor:

    def __init__(self):
        self.root = Tk()
        self.root.title('Just')
        self.root.geometry('800x600')

        self.scroll_y = Scrollbar(self.root)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        
        self.text = Text(self.root)
        self.text.configure(wrap=WORD)
        self.text.pack(side=LEFT, expand=True, fill=BOTH)
        self.text.configure(font=("Times", 16, "normal"))
        self.scroll_y.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll_y.set)

        self.text.configure(background="white", foreground="black")

        self.menubar = Menu(self.root)

        # Menu
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New (Ctrl+n)")
        self.filemenu.add_command(label="Open (Ctrl+o)")
        self.filemenu.add_command(label="Save (Ctrl+s)")
        self.filemenu.add_command(label="Save as (Ctrl+Shift+s)")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit (Ctrl+q)")

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut (Ctrl+x)")
        self.editmenu.add_command(label="Copy (Ctrl+c)")
        self.editmenu.add_command(label="Paste (Ctrl+v)")

        self.settingsmenu = Menu(self.menubar, tearoff=0)
        self.settingsmenu.add_command(label="Increase fontsize (Ctrl++)")
        self.settingsmenu.add_command(label="Decrease fontsize (Ctrl+-)")
        self.settingsmenu.add_separator()
        self.settingsmenu.add_command(label="Light mode (Ctrl+d)")
        self.settingsmenu.add_command(label="Dark mode (Ctrl+l)")
        

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Settings", menu=self.settingsmenu)

        self.root.config(menu=self.menubar)

        self.text.focus()

        self.root.mainloop()

if __name__ == "__main__":
    e = TocEditor()

#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog


class TocEditor:

    def __init__(self):
        self.root = Tk()

        self.root.title('Just')
        self.root.geometry('800x600')

        self.fontsize = 16
        self.filename = ""

        self.scroll_y = Scrollbar(self.root)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        
        self.text = Text(self.root)
        self.text.configure(wrap=WORD)
        self.text.pack(side=LEFT, expand=True, fill=BOTH)
        self.text.configure(font=("Times", self.fontsize, "normal"))
        self.scroll_y.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll_y.set)

        self.text.configure(background="white", foreground="black")

        self.menubar = Menu(self.root)

        # Menu
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New (Ctrl+n)")
        self.filemenu.add_command(label="Open (Ctrl+o)", command=lambda: self.open_file("open"))
        self.filemenu.add_command(label="Save (Ctrl+s)", command=lambda: self.save_file("save"))
        self.filemenu.add_command(label="Save as (Ctrl+Shift+s)", command=lambda: self.save_file_as("save-as"))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit (Ctrl+q)")

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut (Ctrl+x)")
        self.editmenu.add_command(label="Copy (Ctrl+c)")
        self.editmenu.add_command(label="Paste (Ctrl+v)")

        self.settingsmenu = Menu(self.menubar, tearoff=0)
        self.settingsmenu.add_command(label="Increase fontsize (Ctrl++)", command=lambda: self.fontsize_up("up"))
        self.settingsmenu.add_command(label="Decrease fontsize (Ctrl+-)", command=lambda: self.fontsize_down("down"))
        self.settingsmenu.add_separator()
        self.settingsmenu.add_command(label="Light mode (Ctrl+l)", command=lambda: self.light_mode("light"))
        self.settingsmenu.add_command(label="Dark mode (Ctrl+d)", command=lambda: self.dark_mode("dark"))
        

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Settings", menu=self.settingsmenu)

        self.root.config(menu=self.menubar)

        self.root.bind('<Control-l>', self.light_mode)
        self.root.bind('<Control-d>', self.dark_mode)
        self.root.bind('<Control-plus>', self.fontsize_up)
        self.root.bind('<Control-minus>', self.fontsize_down)

        self.root.bind('<Control-o>', self.open_file)
        self.root.bind('<Control-s>', self.save_file)
        self.root.bind('<Control-Shift-S>', self.save_file_as)

        self.text.focus()

        self.root.mainloop()
    
    def dark_mode(self, event):
      self.text.configure(background="black", foreground="white", insertbackground="white")

    def light_mode(self, event):
      self.text.configure(background="white", foreground="black", insertbackground="black")

    def fontsize_up(self, event):
      self.fontsize += 2
      self.text.configure(font=("Times", self.fontsize, "normal"))

    def fontsize_down(self, event):
      self.fontsize -= 2
      self.text.configure(font=("Times", self.fontsize, "normal"))

    def open_file(self, event):
        file_to_read = filedialog.askopenfile(mode="r", filetypes=[("Text files", "*.txt")])
        if file_to_read != None:
          self.text.delete("1.0",END)
          with open(file_to_read.name, 'r') as content:
              for line in content.readlines():
                  self.text.insert(END, line)
          
          self.filename = file_to_read.name
          self.text.mark_set("insert", "%d.%d" % (1, 0))

    def save_file(self, event):
      if self.filename == "":
        filename = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
        #print(filename)
        #print(type(filename))
        if filename != () and filename != "" and filename != None:
          self.filename = filename
          if not self.filename.lower().endswith(".txt"):
            self.filename = self.filename + ".txt"
          if self.filename.endswith(".TXT"):
            self.filename = self.filename[:-4] + ".txt"
      if self.filename != "":
        with open(self.filename, 'w') as file:
          file.write(self.text.get("1.0",END))

    def save_file_as(self, event):
      filename = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
      if filename != () and filename != "" and filename != None:
        self.filename = filename
        if not self.filename.lower().endswith(".txt"):
            self.filename = self.filename + ".txt"
        if self.filename.endswith(".TXT"):
          self.filename = self.filename[:-4] + ".txt"
        with open(self.filename, 'w') as file:
          file.write(self.text.get("1.0",END))

    

if __name__ == "__main__":
    e = TocEditor()

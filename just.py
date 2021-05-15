#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

manual = "Basic functions:\
          \n\
          \nCopy: Ctrl+c\
          \nCut : Ctrl+x\
          \nPaste: Ctrl+p\
          \n\
          \nFontsize up: Ctrl++\
          \nFontsize down: Ctrl+-\
          \n\
          \nDark theme: Ctrl+d\
          \nLight theme: Ctrl+l\
          \n\
          \nSave: Ctrl+s\
          \nSave as: Ctrl+Shift+s\
          \n\
          \nOpen file: Ctrl+o\
          \nNew file: Ctrl+n\
          \nClose: Ctrl+q\
          "

about = "What is Just?:\
          \n\
          \nJust is... just a text editor. It's not a Word Processor \
          \nor an IDE or even a code editor. It's just a text editor, \
          \nnothing more, nothing less.\
          \n\
          \nFeatures include:\
          \n- Cross platform, written in Python with Tkinter\
          \n- Save file / Save file as...\
          \n- Open existing files\
          \n- Create new file\
          \n- Editing works with ctrl+c/x/v\
          \n- Fontsize can be adjusted\
          \n- Dark and Light modes\
          \n\
          \n\
          \nSource code can be found from\
          https://github.com/nikomn/just\
          "

def get_valid_filename():
  filename = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
  if filename == () or filename == "":
    #print("Cancel pressed")
    return ""
  else:
    if not filename.lower().endswith(".txt"):
      filename = filename + ".txt"
    if filename.endswith(".TXT"):
      filename = filename[:-4] + ".txt"
    filename = filename.replace(" ", "_")
    #print("Filename set to", filename)
    return filename


class TocEditor:

    def __init__(self):
        self.root = Tk()

        self.root.title('Just [NEW FILE]')
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
        self.filemenu.add_command(label="New (Ctrl+n)", command=lambda: self.new_file("new"))
        self.filemenu.add_command(label="Open (Ctrl+o)", command=lambda: self.open_file("open"))
        self.filemenu.add_command(label="Save (Ctrl+s)", command=lambda: self.save_file("save"))
        self.filemenu.add_command(label="Save as (Ctrl+Shift+s)", command=lambda: self.save_file_as("save-as"))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit (Ctrl+q)", command=lambda: self.exit_quit("quit"))

        self.settingsmenu = Menu(self.menubar, tearoff=0)
        self.settingsmenu.add_command(label="Increase fontsize (Ctrl++)", command=lambda: self.fontsize_up("up"))
        self.settingsmenu.add_command(label="Decrease fontsize (Ctrl+-)", command=lambda: self.fontsize_down("down"))
        self.settingsmenu.add_separator()
        self.settingsmenu.add_command(label="Light mode (Ctrl+l)", command=lambda: self.light_mode("light"))
        self.settingsmenu.add_command(label="Dark mode (Ctrl+d)", command=lambda: self.dark_mode("dark"))

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help", command=lambda: self.show_help("help"))
        self.helpmenu.add_command(label="About", command=lambda: self.show_about("about"))
        

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Settings", menu=self.settingsmenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar)

        self.root.bind('<Control-l>', self.light_mode)
        self.root.bind('<Control-d>', self.dark_mode)
        self.root.bind('<Control-plus>', self.fontsize_up)
        self.root.bind('<Control-minus>', self.fontsize_down)

        self.root.bind('<Control-n>', self.new_file)
        self.root.bind('<Control-o>', self.open_file)
        self.root.bind('<Control-s>', self.save_file)
        self.root.bind('<Control-Shift-S>', self.save_file_as)
        self.root.bind('<Control-q>', self.exit_quit)

        self.root.protocol("WM_DELETE_WINDOW", self.exit_button_pressed)

        self.text.focus()
        
        self.root.mainloop()
        
    def exit_button_pressed(self):
      self.exit_quit("x")

    def show_help(self, event):
      messagebox.showinfo("Help", manual)

    def show_about(self, event):
      messagebox.showinfo("Just", about)
    
    
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
          self.root.title('Just [' + self.filename + "]")
          self.text.mark_set("insert", "%d.%d" % (1, 0))
          self.text.edit_modified(False)

    def save_file(self, event):
      if self.filename == "":
        filename = get_valid_filename()
        self.filename = filename
      if self.filename != "":
        with open(self.filename, 'w') as file:
          file.write(self.text.get("1.0",END))
        self.root.title('Just [' + self.filename + "]")
        self.text.edit_modified(False)

    def save_file_as(self, event):
      filename = get_valid_filename()
      if filename != "":
        self.filename = filename
        with open(self.filename, 'w') as file:
          file.write(self.text.get("1.0",END))
        self.root.title('Just [' + self.filename + "]")
        self.text.edit_modified(False)

    def new_file(self, event):
      clear_answer_recived = False
      if self.text.edit_modified():
        while not clear_answer_recived:
          confirm = messagebox.askyesnocancel("Unsaved changes", "Unsaved changes found! Do you want to save file before creating new file?")
          if confirm != None:
            if confirm:
              if self.filename == "":
                filename = get_valid_filename()
                self.filename = filename
              if self.filename != "":
                clear_answer_recived = True
                with open(self.filename, 'w') as file:
                  file.write(self.text.get("1.0",END))
            else:
              clear_answer_recived = True
          else:
            clear_answer_recived = True
            
          self.text.delete("1.0",END)
          self.filename = ""
          self.root.title('Just [NEW FILE]')
          self.text.edit_modified(False)
      else:
        self.text.delete("1.0",END)
        self.filename = ""
        self.root.title('Just [NEW FILE]')
        self.text.edit_modified(False)
      
          
    def exit_quit(self, event):
      clear_answer_recived = False
      if self.text.edit_modified():
        while not clear_answer_recived:
          confirm = messagebox.askyesnocancel("Unsaved changes", "Unsaved changes found! Do you want to save before quitting?")
          if confirm != None:
            # Yes / No
            if confirm:
              # Yes
              if self.filename == "":
                filename = get_valid_filename()
                self.filename = filename
              if self.filename != "":
                # Yes, and filename given, all clear
                clear_answer_recived = True
                with open(self.filename, 'w') as file:
                  file.write(self.text.get("1.0",END))
                  self.root.quit()
              else:
                # Yes, but no filename given, unclear what is wanted
                clear_answer_recived = False
            else:
              # No, no saving needed, all clear
              clear_answer_recived = True
              self.root.quit()
          else:
            # Cancel, answer clear, do not close
            clear_answer_recived = True
      else:
        self.root.quit()


if __name__ == "__main__":
    e = TocEditor()

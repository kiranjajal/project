from tkinter import *
import tkFileDialog
from tkinter import filedialog

root=Tk()
path=filedialog.askopenFilename(filetypes=(("template files","*.type")))
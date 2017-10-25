# pylint: disable=C0103,C0111,W0614,W0401
from Tkinter import *
import tkMessageBox
import tkFileDialog
import csv


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def focus_next_window(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def createWidgets(self):
        w, h = 7, 1
        sizeX = 4
        sizeY = 6
        cells = []
        for i in range(sizeY):
            cells.append([])
            for j in range(sizeX):
                cells[i].append([])
        

        for i in range(sizeY):
            cells.append([])
            for j in range(sizeX):
                tmp = Text(self, width=w, height=h)
                tmp.bind("<Tab>", self.focus_next_window)
                tmp.grid(padx=0, pady=0, column=j, row=i)
                cells[i][j] = tmp


def hello():
    tkMessageBox.showinfo("", "Hello!")


def openFile():
    filename = tkFileDialog.askopenfilename(initialdir=".", title="Select file",
                                            filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    with open(filename, "rb") as csvfile:
        rd = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in rd:
            print row


root = Tk()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save as", command=hello)
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)


app = Application()
app.master.title('CSV Editor')
app.master.config(menu=menubar)
app.mainloop()

import tkinter as tk
from tkinter import filedialog, Text
import os


def add_app():
    filename = filedialog.askopenfile(initialdir='/', title='Select file',
                                      filetypes=(('executables', '*.exe'), ('all files', '*.*')))


root = tk.Tk()
canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFileBtn = tk.Button(root, text='Open file', padx=10, pady=5, fg='white', bg='#263D42', command=add_app)
openFileBtn.pack()

runAppsBtn = tk.Button(root, text='Run apps', padx=10, pady=5, fg='white', bg='#263D42')
runAppsBtn.pack()

tk.mainloop()
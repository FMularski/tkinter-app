import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def add_app():
    for widget in frame.winfo_children():   # removing all labels before adding all one again
        widget.destroy()

    filename = filedialog.askopenfile(initialdir='/', title='Select file', # file dialog retuns filename
                                      filetypes=(('executables', '*.exe'), ('all files', '*.*')))
    apps.append(filename.name)

    for app in apps:    # labeling all added apps
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()


def run_apps():
    for app in apps:
        os.startfile(app)   # os.startfile opens app


canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFileBtn = tk.Button(root, text='Open file', padx=10, pady=5, fg='white', bg='#263D42', command=add_app)
openFileBtn.pack()

runAppsBtn = tk.Button(root, text='Run apps', padx=10, pady=5, fg='white', bg='#263D42', command=run_apps)
runAppsBtn.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

tk.mainloop()

with open('save.txt', 'w') as f:   # writing selected apps to text file after closing py app
    for app in apps:
        f.write(app + ',')


import tkinter as tk

def check_key(event):
    key = entry.get()
    if key == "your_secret_key":
        print("Access granted")
    else:
        print("Access denied")

root = tk.Tk()
root.attributes('-fullscreen', True)

label = tk.Label(root, text="Введи ключ и нажми ctrl+c", font=("Arial", 18))
label.pack()

entry = tk.Entry(root, font=("Arial", 16))
entry.pack()

entry.focus_set()

root.bind("<Control-c>", check_key)

root.mainloop()

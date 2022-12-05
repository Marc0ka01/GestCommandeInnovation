import tkinter as tk
from PIL import ImageTk

# initialisation de l'application
t = tk.Tk()

# titre de la fenetre
t.title("Store Gest Ino")

# positionnemt de la fenetre au centre
t.eval("tk::PlaceWindow . center")
x = t.winfo_screenwidth() // 4
y = int(t.winfo_screenheight() * 0.1)
t.geometry("1000x600+" + str(x) + '+' + str(y))

# Frame 1
frame1 = tk.Frame(t, width=1000, height=600)
frame1.grid(row=0, column=0)




























# execution de l'application
t.mainloop()
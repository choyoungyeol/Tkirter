import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("My First GUI")

label = tk.Label(root, text="Hello World !", font=("Arial", 20))

label.pack(padx=20, pady=20)

root.mainloop()

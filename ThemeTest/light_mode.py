import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Light Mode Example")
root.geometry("400x200")
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 10), background="white")
style.configure("TEntry", font=("Segoe UI", 10))
root.configure(bg="white")

ttk.Label(root, text="Light Theme Example").pack(pady=10)
ttk.Entry(root).pack(pady=5)
ttk.Button(root, text="Submit").pack(pady=10)

root.mainloop()

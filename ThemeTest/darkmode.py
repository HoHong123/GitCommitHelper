import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Dark Mode Example")
root.geometry("400x200")
style = ttk.Style()
style.theme_use("clam")
dark_bg = "#2e2e2e"
light_fg = "#f5f5f5"

style.configure("TButton", background=dark_bg, foreground=light_fg, font=("Segoe UI", 10), padding=6)
style.configure("TLabel", background=dark_bg, foreground=light_fg, font=("Segoe UI", 10))
style.configure("TEntry", fieldbackground="#444444", foreground=light_fg, insertcolor=light_fg)
root.configure(bg=dark_bg)

ttk.Label(root, text="Dark Theme Example").pack(pady=10)
ttk.Entry(root).pack(pady=5)
ttk.Button(root, text="Submit").pack(pady=10)

root.mainloop()

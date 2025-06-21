import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GitHub Style Example")
root.geometry("400x200")
style = ttk.Style()
style.theme_use("clam")

bg = "#f6f8fa"
fg = "#24292e"
button_bg = "#2ea44f"
button_fg = "#ffffff"

style.configure("TLabel", background=bg, foreground=fg, font=("Segoe UI", 10))
style.configure("TEntry", fieldbackground="white", foreground=fg, font=("Segoe UI", 10))
style.configure("TButton", background=button_bg, foreground=button_fg, font=("Segoe UI", 10, "bold"), padding=6)
root.configure(bg=bg)

ttk.Label(root, text="GitHub Style Example").pack(pady=10)
ttk.Entry(root).pack(pady=5)
ttk.Button(root, text="Commit").pack(pady=10)

root.mainloop()

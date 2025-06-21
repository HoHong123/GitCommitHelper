from tkinter import ttk

def apply_dark_theme(root):
    root.configure(bg="#2e2e2e")
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", background="#2e2e2e", foreground="#f5f5f5")
    style.configure("TEntry", fieldbackground="#444444", foreground="#f5f5f5", insertcolor="#f5f5f5")
    style.configure("TButton", background="#3c3c3c", foreground="#ffffff", padding=6)
    style.map("TButton", background=[("active", "#505050"), ("pressed", "#2a2a2a")])

import tkinter as tk
from tkinter import ttk
from config import load_format, save_format, load_messages
from constants import ICON_PNG
from clipboard import *
from undo_stack import UndoStack
from event_handler import EventHandler
from utils import get_resource_path
from theme import apply_dark_theme
from PIL import Image, ImageTk
import os

def launch_app():
    root = tk.Tk()
    root.title("Commit Helper")
    root.geometry("900x600")
    root.minsize(600, 400)

    apply_dark_theme(root)

    icon_path = get_resource_path(ICON_PNG)
    if os.path.exists(icon_path):
        try:
            icon = Image.open(icon_path)
            icon_photo = ImageTk.PhotoImage(icon)
            root.iconphoto(True, icon_photo)
        except:
            pass

    main_frame = tk.Frame(root, bg="#2e2e2e")
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=2)
    main_frame.columnconfigure(1, weight=3)
    main_frame.rowconfigure(0, weight=1)

    left_frame = tk.Frame(main_frame, bg="#2e2e2e")
    left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    left_frame.columnconfigure(0, weight=1)
    left_frame.rowconfigure(1, weight=1)

    label = tk.Label(left_frame, text="커밋 메시지를 선택하세요:", bg="#2e2e2e", fg="#f5f5f5")
    label.grid(row=0, column=0, sticky="w")

    canvas = tk.Canvas(left_frame, bg="#2e2e2e", highlightthickness=0)
    scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
    canvas.grid(row=1, column=0, sticky="nsew")
    scrollbar.grid(row=1, column=1, sticky="ns")

    scrollable = tk.Frame(canvas, bg="#2e2e2e")
    window_id = canvas.create_window((0, 0), window=scrollable, anchor="nw")

    scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.itemconfig(window_id, width=e.width))

    scrollable.columnconfigure(0, weight=1)
    for msg in load_messages():
        btn = ttk.Button(scrollable, text=msg)
        btn.config(
            command=lambda m=msg:
            handler.on_message_click(m, title_entry, description_text, format_var, True)
        )
        btn.grid(sticky="ew", padx=2, pady=2)

    right_frame = tk.Frame(main_frame, bg="#2e2e2e")
    right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    right_frame.rowconfigure(3, weight=1)
    right_frame.columnconfigure(0, weight=1)

    top_frame = tk.Frame(right_frame, bg="#2e2e2e")
    top_frame.grid(row=0, column=0, sticky="ew")
    tk.Label(top_frame, text="제목 입력란", bg="#2e2e2e", fg="#f5f5f5").pack(side="left")

    format_var = tk.StringVar(value=load_format())
    drop = ttk.Combobox(top_frame, textvariable=format_var, values=["Git Bash", "VSCode", "GitHub Desktop", "기본"], state="readonly")
    drop.pack(side="right")
    drop.bind("<<ComboboxSelected>>", lambda e: save_format(format_var.get()))

    title_entry = tk.Entry(right_frame)
    title_entry.grid(row=1, column=0, sticky="ew", pady=(0, 10))
    title_undo = UndoStack(title_entry)
    handler = EventHandler(title_undo)
    
    tk.Label(right_frame, text="설명문 입력란", bg="#2e2e2e", fg="#f5f5f5").grid(row=2, column=0, sticky="w")

    text_frame = tk.Frame(right_frame)
    text_frame.grid(row=3, column=0, sticky="nsew")
    scroll = tk.Scrollbar(text_frame)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    description_text = tk.Text(text_frame, wrap="word", yscrollcommand=scroll.set, undo=True, maxundo=-1, bg="#3b3b3b", fg="#f5f5f5", insertbackground="#f5f5f5")
    description_text.pack(fill=tk.BOTH, expand=True)
    description_text.bind("<Tab>", lambda e: handler.handle_tab(e, description_text))
    description_text.bind("<Shift-Tab>", lambda e: handler.handle_tab(e, description_text))
    description_text.bind("<ISO_Left_Tab>", lambda e: handler.handle_tab(e, description_text))
    scroll.config(command=description_text.yview)

    ttk.Button(
        right_frame,
        text="복사하기",
        command=lambda:
            handler.on_message_click("", title_entry, description_text, format_var, False)
    ).grid(row=4, column=0, pady=10, sticky="ew")

    root.bind_all("<Control-z>", handler.handle_undo_redo)
    root.bind_all("<Control-Z>", handler.handle_undo_redo)
    root.bind_all("<Control-y>", handler.handle_undo_redo)
    root.bind_all("<Control-Shift-Z>", handler.handle_undo_redo)

    root.mainloop()
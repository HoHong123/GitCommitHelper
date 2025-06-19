import tkinter as tk
from tkinter import ttk
from config import load_format, save_format
from constants import MESSAGES, ICON_PNG
from clipboard import *
from utils import get_resource_path, today_str
from theme import apply_dark_theme
from PIL import Image, ImageTk
import os
import re

def handle_tab(event, description_text):
    current_line_start = description_text.index("insert linestart")
    current_line_end = description_text.index("insert lineend")
    current_line = description_text.get(current_line_start, current_line_end)

    if event.keysym in ("ISO_Left_Tab", "Tab") and event.state & 0x1:
        if current_line.startswith("+"):
            description_text.delete(current_line_start, f"{current_line_start}+1c")
        return "break"
    elif event.keysym == "Tab":
        description_text.insert(current_line_start, "+")
        return "break"
    
def on_message_click(prefix, title_entry, description_text, format_var, is_left_button):
    if is_left_button:
        original_title = title_entry.get()
        cleaned_title = re.sub(r"^\[[^\]]+\]\s[\u2190-\U0010ffff]+\s\d{2}\.\d{2}\.\d{2}\s*", "", original_title)
        full_title = prefix + today_str() + " " + cleaned_title if prefix != "[Scene] 🎥 Update Scene" else prefix
        title_entry.delete(0, tk.END)
        title_entry.insert(0, full_title)

    fmt = format_var.get()

    if fmt in ["Git Bash", "VSCode"]:
        handle_bash(title_entry, description_text)
    elif is_left_button:
        handle_title(title_entry)
    else:
        handle_body(description_text)

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

    def resize_scrollable(event):
        canvas.itemconfig(window_id, width=event.width)

    scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", resize_scrollable)

    scrollable.columnconfigure(0, weight=1)
    for msg in MESSAGES:
        btn = ttk.Button(scrollable, text=msg)
        btn.config(
            command=lambda m=msg: 
                on_message_click(m, title_entry, description_text, format_var, True)
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

    title_entry = ttk.Entry(right_frame)
    title_entry.grid(row=1, column=0, sticky="ew", pady=(0, 10))

    tk.Label(right_frame, text="설명문 입력란", bg="#2e2e2e", fg="#f5f5f5").grid(row=2, column=0, sticky="w")

    text_frame = tk.Frame(right_frame)
    text_frame.grid(row=3, column=0, sticky="nsew")
    scroll = tk.Scrollbar(text_frame)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    description_text = tk.Text(text_frame, wrap="word", yscrollcommand=scroll.set, undo=True, maxundo=-1, bg="#3b3b3b", fg="#f5f5f5", insertbackground="#f5f5f5")
    description_text.pack(fill=tk.BOTH, expand=True)
    description_text.bind("<Tab>", lambda e: handle_tab(e, description_text))
    description_text.bind("<Shift-Tab>", lambda e: handle_tab(e, description_text))
    description_text.bind("<ISO_Left_Tab>", lambda e: handle_tab(e, description_text))
    scroll.config(command=description_text.yview)

    ttk.Button(
        right_frame,
        text="복사하기",
        command=lambda:
            on_message_click("", title_entry, description_text, format_var, False)
    ).grid(row=4, column=0, pady=10, sticky="ew")

    root.bind("<Control-z>", lambda e: description_text.event_generate("<<Undo>>"))
    root.bind("<Control-Z>", lambda e: description_text.event_generate("<<Undo>>"))
    root.bind("<Control-Shift-Z>", lambda e: description_text.event_generate("<<Redo>>"))
    root.bind("<Control-y>", lambda e: description_text.event_generate("<<Redo>>"))

    root.mainloop()
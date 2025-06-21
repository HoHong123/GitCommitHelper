import os
import tkinter as tk
from tkinter import ttk
from app_config import *
from clipboard import *
from app_config import (
    load_format,
    save_format,
    load_messages,
    load_language,
    save_language
)
from undo_stack import UndoStack
from constants import *
from auto_scrollbar import AutoScrollbar
from theme import apply_dark_theme
from event_handler import EventHandler
from utils import get_resource_path
from PIL import Image, ImageTk
from i18n import get_text

def launch_app():
    root = tk.Tk()
    root.title("Commit Helper")
    root.geometry("900x600")
    root.minsize(600, 400)

    apply_dark_theme(root)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Vertical.TScrollbar", background=SCROLLBAR_BG, troughcolor=SCROLLBAR_TROUGH, arrowcolor=FG_TEXT)

    lang = load_language()
    widgets = {}

    # 메뉴바 생성
    menubar = tk.Menu(root)
    lang_menu = tk.Menu(menubar, tearoff=0)
    lang_menu.add_command(label="한국어", command=lambda: set_language("ko"))
    lang_menu.add_command(label="English", command=lambda: set_language("en"))
    menubar.add_cascade(label="Language", menu=lang_menu)
    root.config(menu=menubar)

    # 메인 프레임
    main_frame = tk.Frame(root, bg=BG_MAIN)
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=2)
    main_frame.columnconfigure(1, weight=3)
    main_frame.rowconfigure(0, weight=1)

    # 왼쪽 프레임 (메시지 버튼)
    left_frame = tk.Frame(main_frame, bg=BG_MAIN)
    left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    left_frame.columnconfigure(0, weight=1)
    left_frame.rowconfigure(1, weight=1)

    label = tk.Label(left_frame, bg=BG_MAIN, fg=FG_TEXT)
    label.grid(row=0, column=0, sticky="w")
    widgets["select_commit"] = label

    canvas = tk.Canvas(left_frame, bg=BG_MAIN, highlightthickness=0)
    scrollbar = AutoScrollbar(left_frame, orient="vertical", command=canvas.yview)
    canvas.grid(row=1, column=0, sticky="nsew")
    scrollbar.grid(row=1, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable = tk.Frame(canvas, bg=BG_MAIN)
    window_id = canvas.create_window((0, 0), window=scrollable, anchor="nw")
    scrollable.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.itemconfig(window_id, width=e.width))
    scrollable.columnconfigure(0, weight=1)

    title_entry = tk.Entry()
    description_text = tk.Text()
    handler = None

    buttons = []
    for msg in load_messages():
        btn = ttk.Button(scrollable, text=msg)
        btn.config(command=lambda m=msg: handler.on_message_click(m, title_entry, description_text, format_var, True))
        btn.grid(sticky="ew", padx=2, pady=2)
        buttons.append(btn)

    # 오른쪽 프레임 (입력 폼)
    right_frame = tk.Frame(main_frame, bg=BG_MAIN)
    right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    right_frame.rowconfigure(3, weight=1)
    right_frame.columnconfigure(0, weight=1)

    top_frame = tk.Frame(right_frame, bg=BG_MAIN)
    top_frame.grid(row=0, column=0, sticky="ew")

    format_var = tk.StringVar(value=load_format())
    drop = ttk.Combobox(top_frame, textvariable=format_var, values=["Git Bash", "VSCode", "GitHub Desktop", "기본"], state="readonly")
    drop.pack(side="right")
    drop.bind("<<ComboboxSelected>>", lambda e: save_format(format_var.get()))

    title_label = tk.Label(top_frame, bg=BG_MAIN, fg=FG_TEXT)
    title_label.pack(side="left")
    widgets["title_input"] = title_label

    title_entry = tk.Entry(right_frame, bg=BG_ENTRY, fg=FG_TEXT, insertbackground=FG_TEXT)
    title_entry.grid(row=1, column=0, sticky="ew", pady=(0, 10))
    title_undo = UndoStack(title_entry)
    handler = EventHandler(title_undo)

    desc_label = tk.Label(right_frame, bg=BG_MAIN, fg=FG_TEXT)
    desc_label.grid(row=2, column=0, sticky="w")
    widgets["description_input"] = desc_label

    text_frame = tk.Frame(right_frame)
    text_frame.grid(row=3, column=0, sticky="nsew")
    text_frame.rowconfigure(0, weight=1)
    text_frame.columnconfigure(0, weight=1)

    scroll = AutoScrollbar(text_frame)
    scroll.grid(row=0, column=1, sticky="ns")

    description_text = tk.Text(
        text_frame,
        wrap="word",
        yscrollcommand=scroll.set,
        undo=True,
        maxundo=-1,
        bg=BG_TEXT,
        fg=FG_TEXT,
        insertbackground=FG_TEXT
    )
    description_text.grid(row=0, column=0, sticky="nsew")
    scroll.config(command=description_text.yview)
    
    description_text.bind("<Tab>", lambda e: handler.handle_tab(e, description_text))
    description_text.bind("<Shift-Tab>", lambda e: handler.handle_tab(e, description_text))
    description_text.bind("<ISO_Left_Tab>", lambda e: handler.handle_tab(e, description_text))


    copy_btn = ttk.Button(
        right_frame,
        command=lambda: handler.on_message_click("", title_entry, description_text, format_var, False)
    )
    copy_btn.grid(row=4, column=0, pady=10, sticky="ew")
    widgets["copy"] = copy_btn

    def update_texts(language):
        widgets["select_commit"].config(text=get_text("select_commit", language))
        widgets["title_input"].config(text=get_text("title_input", language))
        widgets["description_input"].config(text=get_text("description_input", language))
        widgets["copy"].config(text=get_text("copy", language))

    def set_language(language):
        save_language(language)
        update_texts(language)

    update_texts(lang)

    root.bind_all("<Control-z>", handler.handle_undo_redo)
    root.bind_all("<Control-Z>", handler.handle_undo_redo)
    root.bind_all("<Control-y>", handler.handle_undo_redo)
    root.bind_all("<Control-Shift-Z>", handler.handle_undo_redo)

    icon_path = get_resource_path(ICON_PNG)
    if os.path.exists(icon_path):
        try:
            icon = Image.open(icon_path)
            icon_photo = ImageTk.PhotoImage(icon)
            root.iconphoto(True, icon_photo)
        except:
            pass

    root.mainloop()

import tkinter as tk
import re
from utils.formatter import today_str

class EventHandler:
    def __init__(self, title_undo):
        self.title_undo = title_undo

    def handle_tab(self, event, description_text):
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

    def handle_undo_redo(self, event):
        widget = event.widget.focus_get()
        key = event.keysym.lower()
        ctrl = (event.state & 0x4) != 0
        shift = (event.state & 0x1) != 0

        if ctrl and key == "z" and not shift:
            if isinstance(widget, tk.Text):
                widget.event_generate("<<Undo>>")
            elif isinstance(widget, tk.Entry):
                self.title_undo.undo()
            return "break"
        elif ctrl and ((key == "y") or (key == "z" and shift)):
            if isinstance(widget, tk.Text):
                widget.event_generate("<<Redo>>")
            elif isinstance(widget, tk.Entry):
                self.title_undo.redo()
            return "break"

    def on_message_click(self, prefix, title_entry, description_text, format_var, is_left_button):
        if is_left_button:
            original_title = title_entry.get()
            cleaned_title = re.sub(r"^\[[^\]]+\]\s[\u2190-\U0010ffff]+\s\d{2}\.\d{2}\.\d{2}\s*", "", original_title)
            full_title = prefix + today_str() + " " + cleaned_title if prefix != "[Scene] 🎥 Update Scene" else prefix
            title_entry.delete(0, tk.END)
            title_entry.insert(0, full_title)

        fmt = format_var.get()
        if fmt in ["Git Bash", "VSCode"]:
            from core.clipboard import handle_bash
            handle_bash(title_entry, description_text)
        elif is_left_button:
            from core.clipboard import handle_title
            handle_title(title_entry)
        else:
            from core.clipboard import handle_body
            handle_body(description_text)

class UndoStack:
    def __init__(self, entry_widget):
        self.entry = entry_widget
        self.stack = []
        self.redo_stack = []
        self.last_text = self.entry.get()
        self.entry.bind("<KeyRelease>", self.track_change)

    def track_change(self, event=None):
        current = self.entry.get()
        if current != self.last_text:
            self.stack.append(self.last_text)
            self.last_text = current
            self.redo_stack.clear()

    def undo(self):
        if self.stack:
            prev = self.stack.pop()
            self.redo_stack.append(self.entry.get())
            self.entry.delete(0, "end")
            self.entry.insert(0, prev)
            self.last_text = prev

    def redo(self):
        if self.redo_stack:
            next_val = self.redo_stack.pop()
            self.stack.append(self.entry.get())
            self.entry.delete(0, "end")
            self.entry.insert(0, next_val)
            self.last_text = next_val

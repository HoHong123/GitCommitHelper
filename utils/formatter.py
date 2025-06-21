import re
import tkinter as tk
from datetime import datetime

def format_description(text_widget: tk.Text):
    lines = text_widget.get("1.0", tk.END).splitlines()
    formatted, counters = [], [0] * 10
    number_pattern = re.compile(r'^(\d+(?:\.\d+)*)(\.\s|\s)')

    for line in lines:
        stripped = line.lstrip('+').strip()
        level = len(line) - len(line.lstrip('+'))
        match = number_pattern.match(stripped)

        if match:
            levels = list(map(int, match.group(1).split('.')))
            for i, num in enumerate(levels): counters[i] = max(counters[i], num)
            formatted.append(line)
            continue

        if stripped:
            if level == 0:
                counters[0] += 1
                for i in range(1, len(counters)): counters[i] = 0
                num_str = f"{counters[0]}"
            else:
                counters[level] += 1
                for i in range(level + 1, len(counters)): counters[i] = 0
                num_str = '.'.join(str(counters[i]) for i in range(level + 1) if counters[i] > 0)
            formatted.append(f"{num_str}. {stripped}")
        else:
            formatted.append('')

    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", "\n".join(formatted))

def today_str():
    return datetime.today().strftime("%d.%m.%y")

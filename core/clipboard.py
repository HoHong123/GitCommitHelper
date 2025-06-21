import pyperclip
from utils.formatter import format_description, today_str

def handle_title(title_entry):
    title = title_entry.get().strip()
    pyperclip.copy(title or f"[Default] {today_str()}")

def handle_body(description_text):
    format_description(description_text)
    body = description_text.get("1.0", "end").strip()
    pyperclip.copy(body)
    
def handle_bash(title_entry, description_text):
    def escape_quotes(s):
        return s.replace('"', '\\"').replace("'", "\\'")

    title = escape_quotes(title_entry.get().strip())
    format_description(description_text)

    body_raw = description_text.get("1.0", "end").strip()
    lines = body_raw.splitlines()
    body_lines = [escape_quotes(line) + "\\n" for line in lines]
    body = "\n" + "\n".join(body_lines)

    if title and body:
        pyperclip.copy(f'git commit -m "{title}" -m "{body}"')
    elif title:
        pyperclip.copy(f'git commit -m "{title}"')
    elif body:
        pyperclip.copy(f'git commit -m "{body}"')
    else:
        pyperclip.copy(f'git commit -m "[Default] {today_str()}"')

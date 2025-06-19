import json, os

CONFIG_FILE = "config.json"

def load_format():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("format", "GitHub Desktop")
        except:
            pass
    return "GitHub Desktop"

def save_format(value):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"format": value}, f)
    except:
        pass

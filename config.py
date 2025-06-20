import json, os
from constants import MESSAGES

CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "format": "GitHub Desktop",
    "default_messages": MESSAGES
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return DEFAULT_CONFIG

def save_config(config):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    except:
        pass

def load_format():
    return load_config().get("format", "GitHub Desktop")

def save_format(value):
    config = load_config()
    config["format"] = value
    save_config(config)

def load_messages():
    return load_config().get("default_messages", MESSAGES)

def save_messages(messages):
    config = load_config()
    config["default_messages"] = messages
    save_config(config)

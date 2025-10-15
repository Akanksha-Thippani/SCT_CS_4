
from datetime import datetime
import ipywidgets as widgets
from IPython.display import display

ENCRYPTION_KEY = 123
log_entries = []

def encrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

def decrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

input_box = widgets.Text(
    value='',
    placeholder='Type something...',
    description='Input:',
    disabled=False
)

def on_submit(change):
    raw_text = change['new']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {raw_text}"
    encrypted = encrypt(log_entry, ENCRYPTION_KEY)
    log_entries.append(encrypted)
    input_box.value = ''  # Clear input

    print("Encrypted log entry saved.")

input_box.observe(on_submit, names='value')
display(input_box)

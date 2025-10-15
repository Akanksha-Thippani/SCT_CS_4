# Consent Typing Logger

A simple Python program that records lines typed by a consenting user and saves them to a log file. After stopping, the program automatically opens the log file in your default text editor.


## Features

- Logs each typed line with a timestamp.
- Stop the program safely by:
  - Typing `/quit`
  - Pressing **Ctrl+C**
  - Sending EOF (`Ctrl+D` on macOS/Linux, `Ctrl+Z` then Enter on Windows)
- Automatically opens the log file after stopping.
- Beginner-friendly, ethical, and safe — only logs text typed into the program.

---
## Usage

1. Clone or download the repository.
2. Run the Python script:
   ```bash
   python consent_logger_autoopen.p

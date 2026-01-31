# TUI Example in Python

### What It Does:
Just a small terminal app that says back whatever you type. 

Text appears in a scrollable window, and your last entry is shown in a history panel at the bottom (it half works). 

It uses vim-style keybindings for navigation: j/k to scroll, i to focus the input, and escape to switch to scroll mode.

### How To Install:
make sure you have python3 and pip3

```bash
python3 -m venv .venv

source .venv/bin/activate

pip3 install textual rich

python3 demo.py
```

### Tools Used:
I used Textual and Rich. 

### Documentation:
- Textual: https://textual.textualize.io/
- Rich: https://rich.readthedocs.io/

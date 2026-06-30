"""
Smart CCTV Camera — Kunal's Lab
Branded Tkinter desktop control panel for motion detection,
region-based monitoring, recording, and visitor in/out tracking.
"""

import os
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk

from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record

# ── Kunal's Lab brand tokens ──
NAVY        = "#0A0F1E"
NAVY_CARD   = "#161D2F"
NAVY_BORDER = "#1E2A40"
CYAN        = "#00D4FF"
CYAN_DIM    = "#00A8CC"
WHITE       = "#F0F6FF"
GREY        = "#8B9BB4"

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
ICONS_DIR  = os.path.join(ASSETS_DIR, "icons")

window = tk.Tk()
window.title("Smart CCTV — Kunal's Lab")
window.configure(bg=NAVY)

icon_path = os.path.join(ASSETS_DIR, "mn.png")
if os.path.exists(icon_path):
    window.iconphoto(False, tk.PhotoImage(file=icon_path))

window.attributes('-fullscreen', True)
window.bind('<Escape>', lambda e: window.attributes('-fullscreen', False))

# ── Header ──
header = tk.Frame(window, bg=NAVY)
header.pack(fill='x', pady=(30, 10))

brand_font = font.Font(size=13, weight='bold', family='Helvetica')
tag_font   = font.Font(size=9, family='Courier')

tk.Label(header, text="KUNAL'S LAB", font=brand_font, fg=CYAN, bg=NAVY).pack()
tk.Label(header, text="AI · ML · SYSTEMS", font=tag_font, fg=GREY, bg=NAVY).pack(pady=(2, 0))

# ── Title ──
title_font = font.Font(size=32, weight='bold', family='Helvetica')
tk.Label(window, text="Smart CCTV Camera", font=title_font, fg=WHITE, bg=NAVY).pack(pady=(20, 4))

sub_font = font.Font(size=11, family='Helvetica')
tk.Label(window, text="Motion Detection · Region Monitoring · Visitor Tracking",
         font=sub_font, fg=GREY, bg=NAVY).pack(pady=(0, 30))

# ── Card container for the icon ──
icon_card = tk.Frame(window, bg=NAVY_CARD, highlightbackground=NAVY_BORDER, highlightthickness=1)
icon_card.pack(pady=(0, 30))

spy_icon_path = os.path.join(ICONS_DIR, "spy.png")
if os.path.exists(spy_icon_path):
    spy_img = Image.open(spy_icon_path).resize((110, 110), Image.LANCZOS)
    spy_photo = ImageTk.PhotoImage(spy_img)
    tk.Label(icon_card, image=spy_photo, bg=NAVY_CARD).pack(padx=30, pady=20)

# ── Button frame ──
btn_frame = tk.Frame(window, bg=NAVY)
btn_frame.pack(pady=10)


def load_icon(name, size=(32, 32)):
    path = os.path.join(ICONS_DIR, name)
    if not os.path.exists(path):
        return None
    img = Image.open(path).resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)


# Keep references alive
_icon_refs = {}
_icon_refs['monitor']  = load_icon('lamp.png')
_icon_refs['region']   = load_icon('rectangle-of-cutted-line-geometrical-shape.png')
_icon_refs['record']   = load_icon('recording.png')
_icon_refs['visitor']  = load_icon('incognito.png')
_icon_refs['exit']     = load_icon('exit.png')

btn_font = font.Font(size=12, weight='bold', family='Helvetica')


def make_button(parent, text, command, icon_key, accent=CYAN):
    btn = tk.Button(
        parent,
        text=f"  {text}",
        image=_icon_refs.get(icon_key),
        compound='left',
        command=command,
        font=btn_font,
        fg=NAVY,
        bg=accent,
        activebackground=CYAN_DIM,
        activeforeground=NAVY,
        bd=0,
        relief='flat',
        height=2,
        width=18,
        cursor='hand2',
        padx=10,
    )
    return btn


buttons = [
    ("Monitor",       noise,        'monitor'),
    ("Region Select", rect_noise,   'region'),
    ("Record",        record,       'record'),
    ("Visitor Log",   in_out,       'visitor'),
]

for i, (label, cmd, key) in enumerate(buttons):
    b = make_button(btn_frame, label, cmd, key)
    b.grid(row=i // 2, column=i % 2, padx=16, pady=12)

# ── Exit button (distinct styling) ──
exit_frame = tk.Frame(window, bg=NAVY)
exit_frame.pack(pady=(20, 10))

exit_btn = tk.Button(
    exit_frame,
    text="  Exit",
    image=_icon_refs.get('exit'),
    compound='left',
    command=window.quit,
    font=btn_font,
    fg=WHITE,
    bg=NAVY_CARD,
    activebackground="#FF6B6B",
    activeforeground=WHITE,
    bd=1,
    highlightbackground=NAVY_BORDER,
    relief='flat',
    height=2,
    width=18,
    cursor='hand2',
)
exit_btn.pack()

# ── Footer ──
footer_font = font.Font(size=8, family='Courier')
tk.Label(window, text="Kunal's Lab · AI & ML Systems · Press Esc to exit fullscreen",
         font=footer_font, fg=GREY, bg=NAVY).pack(side='bottom', pady=20)

window.mainloop()

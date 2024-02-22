import tkinter as tk
import psutil
import os
import fflags_updater

def open_roblox():
    print("Opening Roblox Player")
    os.system("open /Applications/Roblox.app")

def close_roblox():
    for proc in psutil.process_iter(['pid', 'name']):
        if "roblox" in proc.info['name'].lower():
            print(f"Terminating Roblox Process (PID: {proc.info['pid']})")
            os.kill(proc.info['pid'], 9)

def update_fflags():
    fflags_updater.updateFFlags()

def change_flags():
    flags_window = tk.Tk()
    flags_window.title("Change FFlags")

    # Scrollable Frame
    canvas = tk.Canvas(flags_window)
    scrollbar = tk.Scrollbar(flags_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Read Flags from the text file
    flags_text = ""
    with open("FVariables.txt", "r") as file:
        flags_text = file.read()

    flags_label = tk.Label(scrollable_frame, text=flags_text)
    flags_label.pack()

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    flags_window.mainloop()

# Create a new window
window = tk.Tk()
window.title("Mac Roblox Bootstrapper")

open_roblox_button = tk.Button(window, text="Open Roblox", command=open_roblox)
open_roblox_button.pack()

close_roblox_button = tk.Button(window, text="Close Roblox", command=close_roblox)
close_roblox_button.pack()

fflags_button = tk.Button(window, text="Update FFlags", command=update_fflags)
fflags_button.pack()

change_flags_button = tk.Button(window, text="Change FFlags", command=change_flags)
change_flags_button.pack()

# Run the main loop
window.mainloop()

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

# Create a new window
window = tk.Tk()
window.title("Mac Roblox Bootstrapper")

open_roblox_button = tk.Button(window, text="Open Roblox", command=open_roblox)
open_roblox_button.pack()

close_roblox_button = tk.Button(window, text="Close Roblox", command=close_roblox)
close_roblox_button.pack()

fflags_button = tk.Button(window, text="Update FFlags", command=update_fflags)
fflags_button.pack()

# Run the main loop
window.mainloop()
import tkinter as tk
import psutil
import os
import fflags_updater
import requests
import re

def open_roblox():
    print("Opening Roblox Player")
    os.system("open /Applications/Roblox.app")

def close_roblox():
    for proc in psutil.process_iter(["pid", "name"]):
        if "roblox" in proc.info["name"].lower():
            print(f"Terminating Roblox Process (PID: {proc.info['pid']})")
            os.kill(proc.info["pid"], 9)

def update_fflags():
    fflags_updater.updateFFlags()

behavior_map = {
    "F": "Fast",
    "DF": "Dynamic Fast",
    "SF": "Synchronized Fast"
}
type_map = {
    "Flag": "bool",
    "Int": "int",
    "String": "string",
    "Log": "byte",
}

def change_flags():
    flags_window = tk.Tk()
    flags_window.title("Change FFlags")

    # Scrollable Frame
    canvas = tk.Canvas(flags_window)
    scrollbar = tk.Scrollbar(flags_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Fetch Flags from the provided URL
    fflags_url = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/FVariables.txt"
    response = requests.get(fflags_url)
    flags_text = response.text

    fflags = flags_text.splitlines()

    # Process each FFlag entry
    for fflag in fflags:
        processed_fflag_name = re.sub(r"\[.*?\]\s", "", fflag)

        behaviour = None
        for behaviorId, behaviorName in behavior_map.items():
            if processed_fflag_name.startswith(behaviorId):
                behaviour = behaviorId
        if not behaviour:
            continue

        fflag_name_without_behavior = processed_fflag_name[len(behaviour):]

        data_type = None
        for typeId, typeName in type_map.items():
            if fflag_name_without_behavior.startswith(typeId):
                data_type = typeName
        if not data_type:
            continue

        fflag_real_name = fflag_name_without_behavior[len(data_type):]

        print(f"Flag: {data_type}, Name: {fflag_real_name}, Datatype: {data_type}")
        if data_type == "bool":
            tk.Checkbutton(scrollable_frame, text=fflag_real_name).pack()
        elif data_type == "int" or data_type == "string" or data_type == "byte":
            tk.Label(scrollable_frame, text=fflag_real_name).pack()
        tk.Entry(scrollable_frame).pack()

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

# Put window on top
window.lift()
window.call("wm", "attributes", ".", "-topmost", True)
window.after_idle(window.call, "wm", "attributes", ".", "-topmost", False)

# Run the main loop
window.mainloop()

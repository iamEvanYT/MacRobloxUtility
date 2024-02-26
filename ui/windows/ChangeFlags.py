import tkinter as tk
import re
import os
import sys
import threading
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '...')))
from utils.constants import *
from utils.LoadFFlags import loadFFLags
from alive_progress import alive_bar

found_fflags = {}

def ChangeFlagsWindow():
    flags_window = tk.Toplevel()
    flags_window.title("Change FFlags")
    flags_window.geometry("500x500")

    # Scrollable Frame
    canvas = tk.Canvas(flags_window)
    scrollbar = tk.Scrollbar(flags_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Fetch Flags from LoadFFLags
    fflags = loadFFLags()

    # Process each FFlag entry
    with alive_bar(len(fflags)) as bar:
        for fflag in fflags:
            processed_fflag_name = re.sub(r"\[.*?\]\s", "", fflag)

            behaviour = None
            for behaviorId, behaviorName in BEHAVIOR_MAP.items():
                if processed_fflag_name.startswith(behaviorId):
                    behaviour = behaviorId
            if not behaviour:
                continue

            # Synchronized Fast Flags can only be updated on the server
            if (behaviour == "SF"):
                continue

            fflag_name_without_behavior = processed_fflag_name[len(behaviour):]

            data_type = None
            for typeId, typeName in TYPE_MAP.items():
                if fflag_name_without_behavior.startswith(typeId):
                    data_type = typeName
            if not data_type:
                continue

            fflag_real_name = fflag_name_without_behavior[len(data_type):]

            #print(f"Flag: {data_type}, Name: {fflag_real_name}, Datatype: {data_type}")
            found_fflags[fflag_real_name] = data_type
            if data_type == "bool":
                tk.Checkbutton(scrollable_frame, text=fflag_real_name).pack()
            elif data_type == "int" or data_type == "string" or data_type == "byte":
                tk.Label(scrollable_frame, text=fflag_real_name).pack()
            tk.Entry(scrollable_frame).pack()
            bar()

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    flags_window.mainloop()
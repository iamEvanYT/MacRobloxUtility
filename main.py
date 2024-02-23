import tkinter as tk
from flags.fflags_updater import updateFFlags
from utils.roblox import *
from ui.windows import ChangeFlags
from utils.LoadFFlags import *
import threading

## FPS UNLOCKER OPTIONS ##
# "FFlagGameBasicSettingsFramerateCap": true,
# "DFIntTaskSchedulerTargetFps": 10000,

## Force Vulkan Renderer ##
# "FFlagDebugGraphicsDisableMetal": true,
# "FFlagDebugGraphicsPreferVulkan":"true",
# "FFlagDebugGraphicsDisableDirect3D11":"true"

if __name__ == "__main__":
    loadFFLags()
    # Create a new window
    window = tk.Tk()
    window.title("Mac Roblox Bootstrapper")
    window.geometry("500x500")

    open_roblox_button = tk.Button(window, text="Open Roblox", command=open_roblox)
    open_roblox_button.pack()

    close_roblox_button = tk.Button(window, text="Close Roblox", command=close_roblox)
    close_roblox_button.pack()

    fflags_button = tk.Button(window, text="Update FFlags", command=threading.Thread(target=updateFFlags).start)
    fflags_button.pack()

    change_flags_button = tk.Button(window, text="Change FFlags", command=threading.Thread(target=ChangeFlags.ChangeFlagsWindow).start)
    change_flags_button.pack()

    # Put window on top
    window.lift()
    window.call("wm", "attributes", ".", "-topmost", True)
    window.after_idle(window.call, "wm", "attributes", ".", "-topmost", False)

    # Run the main loop
    window.mainloop()

import os, subprocess, psutil, platform

def is_windows():
    return platform.system() == "Windows"

def is_mac():
    return platform.system() == "Mac"

def open_roblox():
    print("Opening Roblox Player")
    print("start roblox:///" if is_windows() else ["open", "/Applications/Roblox.app"])
    if is_windows():
        os.system('cmd /C "start roblox:///"')
    else:
        subprocess.call(["open","/Applications/Roblox.app/Contents/MacOS/RobloxPlayer"])
        #subprocess.run(["open", "/Applications/Roblox.app"], check=True)

def close_roblox():
    for proc in psutil.process_iter(["pid", "name"]):
        if "roblox" in proc.info["name"].lower():
            print(f"Terminating Roblox Process (PID: {proc.info['pid']})")
            os.kill(proc.info["pid"], 9)
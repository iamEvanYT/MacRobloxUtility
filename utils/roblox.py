import os, subprocess, psutil, platform, time

def is_windows():
    return platform.system() == "Windows"

def is_mac():
    print(platform.system())
    return platform.system() == "Darwin"

def mac_bypass_single_roblox():
    subprocess.run(["open", "/Applications/Roblox.app"], check=True)
    time.sleep(1)
    for proc in psutil.process_iter(["pid", "name"]):
        if "roblox" in proc.info["name"].lower():
            print(f"Terminating Roblox Process (PID: {proc.info['pid']})")
            os.kill(proc.info["pid"], 9)

def bypass_single_roblox():
    if is_mac():
        mac_bypass_single_roblox()
    elif is_windows():
        return Exception("Does not support Windows yet.")

def open_roblox():
    print("Opening Roblox Player")
    print("start roblox:///" if is_windows() else ["open", "/Applications/Roblox.app"])
    if is_windows():
        os.system('cmd /C "start roblox:///"')
    else:
        subprocess.call(["open","/Applications/Roblox.app/Contents/MacOS/RobloxPlayer"])

def close_roblox():
    for proc in psutil.process_iter(["pid", "name"]):
        if "roblox" in proc.info["name"].lower():
            print(f"Terminating Roblox Process (PID: {proc.info['pid']})")
            os.kill(proc.info["pid"], 9)
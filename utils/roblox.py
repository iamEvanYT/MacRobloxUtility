import os, subprocess, psutil, platform, time
DEVNULL = subprocess.DEVNULL

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
    if is_windows():
        os.system('cmd /C "start roblox:///"')
    else:
        subprocess.Popen("/Applications/Roblox.app/Contents/MacOS/RobloxPlayer; exit;", shell=True, stdout=DEVNULL, stderr=DEVNULL)

def close_roblox():
    for proc in psutil.process_iter(["pid", "name"]):
        if "roblox" in proc.info["name"].lower():
            print(f"Terminating Roblox Process (PID: {proc.info['pid']})")
            os.kill(proc.info["pid"], 9)
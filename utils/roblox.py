import os, subprocess, psutil

def open_roblox():
    print("Opening Roblox Player")
    subprocess.run(["open", "/Applications/Roblox.app"], check=True)

def close_roblox():
    for proc in psutil.process_iter(["pid", "name"]):
        if "roblox" in proc.info["name"].lower():
            print(f"Terminating Roblox Process (PID: {proc.info['pid']})")
            os.kill(proc.info["pid"], 9)
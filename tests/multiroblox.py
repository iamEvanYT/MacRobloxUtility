import ctypes

def main():
    # Create a mutex
    mutex = ctypes.windll.kernel32.CreateMutexW(None, True, "ROBLOX_singletonMutex")

    # Check if mutex creation failed
    if ctypes.windll.kernel32.GetLastError() == 183:  # ERROR_ALREADY_EXISTS
        print("Another instance of ROBLOX is already running.")
    else:
        print("You can now use multiple ROBLOX clients. Closing this will cause all ROBLOX clients to terminate except for one.")

    print("Press any key to close")
    input()

if __name__ == "__main__":
    main()
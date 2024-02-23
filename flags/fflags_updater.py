import os
import json

def getFflagsData(fflags_file_path=os.path.join(os.getcwd(),"/config/fflags.json")):
    # Create a JSON file called ClientAppSettings.json in the ClientSettings folder
    fflags_data = {}
    if os.path.exists(fflags_file_path):
        with open(fflags_file_path, "r") as file:
            fflags_data = json.load(file)
            return fflags_data
    else:
        raise Exception("Config fflags not found. Please configure it in the config folder.")

def updateFFlags():
    # Change directory to /Applications/Roblox.app/Contents/MacOS
    os.chdir("/Applications/Roblox.app/Contents/MacOS")

    # Check if the folder "ClientSettings" exists, and create it if it doesn't
    client_settings_folder = "ClientSettings"
    if not os.path.exists(client_settings_folder):
        os.makedirs(client_settings_folder)

    # Get the fflags data
    fflags_data = getFflagsData()

    file_path = os.path.join(client_settings_folder, "ClientAppSettings.json")
    with open(file_path, "w") as file:
        json.dump(fflags_data, file, indent=4)

    print("ClientAppSettings.json has been created in the ClientSettings folder.")
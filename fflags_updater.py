import os
import json

def updateFFlags():
    current_directory = os.getcwd()
    fflags_file_path = os.path.join(current_directory,"fflags.json")

    # Change directory to /Applications/Roblox.app/Contents/MacOS
    os.chdir("/Applications/Roblox.app/Contents/MacOS")

    # Check if the folder "ClientSettings" exists, and create it if it doesn't
    client_settings_folder = "ClientSettings"
    if not os.path.exists(client_settings_folder):
        os.makedirs(client_settings_folder)

    # Create a JSON file called ClientAppSettings.json in the ClientSettings folder
    fflags_data = {}
    if os.path.exists(fflags_file_path):
        with open(fflags_file_path, "r") as file:
            fflags_data = json.load(file)

    file_path = os.path.join(client_settings_folder, "ClientAppSettings.json")
    with open(file_path, "w") as file:
        json.dump(fflags_data, file, indent=4)

    print("ClientAppSettings.json has been created in the ClientSettings folder.")
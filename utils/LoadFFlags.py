import re
import requests
from .constants import *
from alive_progress import alive_bar

def loadFFLags():
    # Fetch Flags from the provided URL
    fflags_url = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/FVariables.txt"
    response = requests.get(fflags_url)
    flags_text = response.text

    processing_fflags = flags_text.splitlines()
    fflags = []

    # Process each FFlag entry
    with alive_bar(len(processing_fflags)) as bar:
        for fflag in processing_fflags:
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
            bar()
            
            fflags.append({
                'behaviour': behaviour,
                'name': processed_fflag_name,
                'type': data_type
            })

    return fflags
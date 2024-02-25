## FPS UNLOCKER OPTIONS ##
# "FFlagGameBasicSettingsFramerateCap": true,
# "DFIntTaskSchedulerTargetFps": 10000,

## Force Vulkan Renderer ##
# "FFlagDebugGraphicsDisableMetal": true,
# "FFlagDebugGraphicsPreferVulkan":"true",
# "FFlagDebugGraphicsDisableDirect3D11":"true"

import subprocess

node_frontend_process = subprocess.Popen(args = ["npm", "start"], cwd = "./frontend/")
python_backend_process = subprocess.Popen(["python3", "web.py"])

try:
    while True:
        pass
except KeyboardInterrupt:
    node_frontend_process.terminate()
    python_backend_process.terminate()
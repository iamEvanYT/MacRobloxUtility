## FPS UNLOCKER OPTIONS ##
# "FFlagGameBasicSettingsFramerateCap": true,
# "DFIntTaskSchedulerTargetFps": 10000,

## Force Vulkan Renderer ##
# "FFlagDebugGraphicsDisableMetal": true,
# "FFlagDebugGraphicsPreferVulkan":"true",
# "FFlagDebugGraphicsDisableDirect3D11":"true"

import subprocess, signal, time

python_backend_process = subprocess.Popen(["python3", "web.py"]) # Py for python 1.12 python for python<1.12
time.sleep(1.5)

node_frontend_process = subprocess.Popen("npm start", cwd = "./frontend/", shell=True)

try:
    while True:
        pass
except KeyboardInterrupt:
    node_frontend_process.send_signal(signal.SIGTERM)
    python_backend_process.send_signal(signal.SIGTERM)
    time.sleep(1)
    node_frontend_process.terminate()
    python_backend_process.terminate()
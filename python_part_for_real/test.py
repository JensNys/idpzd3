import os
import time

port = "8085"
# Start the server in the background and capture its PID
os.system(f"python3 -m http.server {port} & echo $! > server_pid.txt")
# Give it a moment to start
time.sleep(1)
# Open Firefox to the html
os.system(f"firefox http://localhost:{port}/out/index.html &")
# Let the server run for 10 seconds
time.sleep(2)
# Kill the server
with open("server_pid.txt") as f:
    pid = f.read().strip()
os.system(f"kill {pid}")
os.remove("server_pid.txt")


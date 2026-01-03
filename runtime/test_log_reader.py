import time
import os

# Default Log Path for Windows
# You might need to adjust this depending on where Hearthstone is installed
# Standard path: C:\Program Files (x86)\Hearthstone\Logs\Power.log
# OR sometimes in AppData on recent versions? 
# Usually logs are next to the executable or in AppData/Local/Blizzard/Hearthstone/Logs?
# The log.config is in AppData, but the Logs are usually in the installation folder.

POSSIBLE_ROOTS = [
    r"E:\JEU\Hearthstone\Logs",
    r"C:\Program Files (x86)\Hearthstone\Logs",
]

def find_power_log():
    for root in POSSIBLE_ROOTS:
        if not os.path.exists(root):
            continue
            
        # Check for Power.log directly
        direct_path = os.path.join(root, "Power.log")
        if os.path.exists(direct_path):
            return direct_path
            
        # Check subdirectories (recent timestamps)
        subdirs = [os.path.join(root, d) for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
        if not subdirs:
            continue
            
        # Sort by modification time (newest first)
        subdirs.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        
        # Look in newest folder
        for latest_dir in subdirs:
            log_path = os.path.join(latest_dir, "Power.log")
            if os.path.exists(log_path):
                return log_path
                
    return None

def follow(thefile):
    """Generator that yields new lines in a file"""
    thefile.seek(0, 2) # Go to the end
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == "__main__":
    log_path = find_power_log()
    
    # If not found, let's look for ANY log file in standard dirs to be sure
    if not log_path:
        print("Could not find Power.log in standard locations.")
        print("Please specify the path manually in the code.")
        # Attempt to prompt? No, interactive mode might fail.
        # Just create a dummy one for testing if not found?
        # Simulation Mode
        print("Creating dummy log for testing...")
        with open("dummy_power.log", "w") as f:
            f.write("DUMMY LOG START\n")
        log_path = "dummy_power.log"
    
    print(f"Watching Log File: {log_path}")
    print("Waiting for new lines... (Open Hearthstone and play a card to see generic logs)")
    
    try:
        with open(log_path, "r", encoding="utf-8") as file:
            # If it's a dummy log, we simulate writing to it in a separate process or usually user does it.
            # But for Real HS, the game writes to it.
            
            # Print last 5 lines first
            file.seek(0, 2)
            end_pos = file.tell()
            # Simple tail not efficient for huge files but ok here
            
            lines_generator = follow(file)
            for line in lines_generator:
                if "PowerTaskList.DebugPrintPower" in line or "BLOCK_START" in line or "TAG_CHANGE" in line:
                    print(line.strip())
                    
    except KeyboardInterrupt:
        print("\nStopping watcher.")

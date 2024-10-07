import platform
from tasks import run_task

def gather_system_info():
    sys_info = {
        'os': platform.system(),
        'release': platform.release(),
        'machine': platform.machine(),
    }
    return sys_info

def start_tool():
    print("Welcome to the CTF All-in-One Tool")
    sys_info = gather_system_info()
    print(f"Detected system: {sys_info}")
    
    task = input("What task would you like to run? (e.g., nmap, metasploit, sqlmap, nikto, burpsuite): ")
    run_task(task, sys_info)
        
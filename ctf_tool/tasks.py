from metasploit import run_metasploit
from nmap import run_nmap
from sqlmap import run_sqlmap
from nikto import run_nikto
from burpsuite import run_burpsuite

def run_task(task, sys_info):
    if task.lower() == 'metasploit':
        run_metasploit(sys_info)
    elif task.lower() == 'nmap':
        run_nmap(sys_info)
    elif task.lower() == 'sqlmap':
        run_sqlmap(sys_info)
    elif task.lower() == 'nikto':
        run_nikto(sys_info)
    elif task.lower() == 'burpsuite':
        run_burpsuite(sys_info)
    else:
        print(f"Task {task} not recognized. Please try again.")
        
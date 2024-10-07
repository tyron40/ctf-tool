import subprocess
import time

def run_burpsuite(sys_info):
    print("Launching Burp Suite...")
    target = input("Enter the target URL (e.g., http://example.com): ")
    scan_type = input("Do you want to launch Burp Suite manually, or perform an automated scan? (manual/auto): ")

    if scan_type == 'auto':
        print("Launching automated scan requires Burp Suite Pro with API access. For now, launching Burp Suite manually.")
        print("You'll be able to configure the scan manually via the GUI.")
    else:
        print("Launching Burp Suite in GUI mode. You can configure your tests manually.")

    print("Burp Suite is starting...")
    subprocess.Popen(['java', '-jar', '/path/to/burpsuite_community.jar'])
    time.sleep(10)
    print("Burp Suite has been launched. You can now start your scan manually.")
        
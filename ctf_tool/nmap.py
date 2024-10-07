import subprocess

def run_nmap(sys_info):
    print("You have chosen to run Nmap.")
    
    target = input("Please enter the target (website or IP address): ")
    scan_type = input("What type of scan would you like to run? (e.g., 'quick', 'full', 'vuln'): ")

    if scan_type == 'quick':
        nmap_command = ['nmap', '-T4', target]
    elif scan_type == 'full':
        nmap_command = ['nmap', '-p-', target]
    elif scan_type == 'vuln':
        nmap_command = ['nmap', '--script=vuln', target]
    else:
        print("Unknown scan type. Running quick scan by default.")
        nmap_command = ['nmap', '-T4', target]

    result = subprocess.run(nmap_command, capture_output=True, text=True)
    print("Scan completed. Here are the results:")
    print(result.stdout)

    vulnerabilities = parse_nmap_output(result.stdout)
    display_vulnerabilities(vulnerabilities)
    save_report(target, vulnerabilities)

def parse_nmap_output(output):
    vulnerabilities = []
    if "CVE-" in output:
        vulnerabilities.append("Potential CVE found in the output.")
    if "open port" in output:
        vulnerabilities.append("Open port detected.")
    return vulnerabilities

def save_report(target, vulnerabilities):
    report_filename = f"{target}_nmap_report.txt"
    with open(report_filename, 'w') as report_file:
        report_file.write("Vulnerability Report for " + target + "\n")
        if vulnerabilities:
            for v in vulnerabilities:
                report_file.write(f"- {v}\n")
        else:
            report_file.write("No vulnerabilities detected.\n")
    print(f"Report saved as {report_filename}")
        
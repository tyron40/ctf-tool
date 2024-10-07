import subprocess

def run_nikto(sys_info):
    print("Running Nikto...")
    target = input("Please enter the target website: ")

    nikto_command = ['nikto', '-h', target]

    result = subprocess.run(nikto_command, capture_output=True, text=True)
    print("Nikto scan completed. Here are the results:")
    print(result.stdout)

    vulnerabilities = parse_nikto_output(result.stdout)
    display_vulnerabilities(vulnerabilities)
    save_report(target, vulnerabilities)

def parse_nikto_output(output):
    vulnerabilities = []
    if "vulnerable" in output.lower():
        vulnerabilities.append("Possible web server vulnerability detected.")
    return vulnerabilities

def save_report(target, vulnerabilities):
    report_filename = f"{target}_nikto_report.txt"
    with open(report_filename, 'w') as report_file:
        report_file.write("Vulnerability Report for " + target + "\n")
        if vulnerabilities:
            for v in vulnerabilities:
                report_file.write(f"- {v}\n")
        else:
            report_file.write("No vulnerabilities detected.\n")
    print(f"Report saved as {report_filename}")
        
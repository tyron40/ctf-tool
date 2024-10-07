import subprocess

def run_sqlmap(sys_info):
    print("Running SQLMap...")
    target = input("Please enter the target URL: ")
    sqlmap_command = ['sqlmap', '-u', target, '--batch']

    result = subprocess.run(sqlmap_command, capture_output=True, text=True)
    print("SQLMap scan completed. Here are the results:")
    print(result.stdout)

    vulnerabilities = parse_sqlmap_output(result.stdout)
    display_vulnerabilities(vulnerabilities)
    save_report(target, vulnerabilities)

def parse_sqlmap_output(output):
    vulnerabilities = []
    if "sql injection" in output.lower():
        vulnerabilities.append("SQL Injection vulnerability detected.")
    return vulnerabilities

def save_report(target, vulnerabilities):
    report_filename = f"{target}_sqlmap_report.txt"
    with open(report_filename, 'w') as report_file:
        report_file.write("Vulnerability Report for " + target + "\n")
        if vulnerabilities:
            for v in vulnerabilities:
                report_file.write(f"- {v}\n")
        else:
            report_file.write("No vulnerabilities detected.\n")
    print(f"Report saved as {report_filename}")
        
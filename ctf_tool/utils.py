import re

def display_vulnerabilities(vulnerabilities):
    if vulnerabilities:
        print("\nVulnerabilities found:")
        for v in vulnerabilities:
            print(f"- {v}")
    else:
        print("\nNo known vulnerabilities found.")
        
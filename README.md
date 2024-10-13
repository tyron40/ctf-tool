CTF All-in-One Tool 
Description

This tool is designed to simplify penetration testing by automating key tasks using popular tools such as Nmap, Metasploit, SQLMap, Nikto, and Burp Suite. It features an easy-to-use command-line interface (CLI) that guides users through scanning, exploitation, and vulnerability reporting tasks.

Features

- **Nmap**: Network scanning and vulnerability detection.
- **Metasploit**: Exploit testing.
- **SQLMap**: SQL injection vulnerability testing.
- **Nikto**: Web server vulnerability scanning.
- **Burp Suite**: Manual or automated web application security testing.

Installation and Setup

1. **Clone the Project**:
   - Download the project or clone the repository:
   ```bash
   git clone https://github.com/tyron40/ctf-tool.git
   cd ctf-tool
   ```

2. **Set Up Python Virtual Environment** (Optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   .\venv\Scripts\activate  # For Windows
   ```

3. **Install the Required Dependencies**:
   If any Python libraries are required, install them with `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up in Visual Studio Code**:
   - Open Visual Studio Code and open the `ctf-tool` folder.
   - Ensure the Python extension is installed.

5. **Install the CTF Tool Package** (Optional):
   If you want to install the tool package to the system:
   ```bash
   sudo python3 setup.py install
   ```

6. **Run the Tool**:
   ```bash
   python3 cli.py
   ```

Usage in Kali Linux

1. **Ensure Necessary Tools are Installed**:
   Make sure the following tools are installed:
   - **Nmap**: `sudo apt install nmap`
   - **Metasploit**: `sudo apt install metasploit-framework`
   - **SQLMap**: `sudo apt install sqlmap`
   - **Nikto**: `sudo apt install nikto`
   - **Burp Suite**: Pre-installed in most Kali distributions, or download from [Burp Suite Community](https://portswigger.net/burp/communitydownload).

2. **Run the Tool on Kali**:
   ```bash
   python3 cli.py
   ```
   Follow the prompts to select and configure the scans.

Example Use

Example running Nmap and SQLMap from the CLI:
```bash
python3 cli.py
# Choose Nmap and follow the prompts
# Choose SQLMap and follow the prompts
```

Contributing and License

Feel free to submit pull requests or open issues to improve this tool.

This project is licensed under the MIT License.


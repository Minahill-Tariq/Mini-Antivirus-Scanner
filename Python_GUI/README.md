# Python GUI Frontend (Tkinter)

A dark-themed desktop application built with **Python 3** and **Tkinter** that provides interactive file browsing, multi-rule threat detection, real-time reporting, and dynamic quarantine logging

---

## 🔑 Default Credentials

The application includes pre-configured credentials alongside a functional user registration (Sign Up) workflow

* **Default Username:** `minahil`
* **Default Password:** `1234`

---

## 🛠️ Features & Mechanics

* **Authentication System:** Includes login validation and dynamic in-memory account creation
* **Three-Tier Scanning Engine:**
  * **Filename Inspection:** Scans file basenames for high-risk malware keywords (e.g., `virus`, `hack`, `malware`, `trojan`, `rootkit`, `backdoor`)
  * **Extension Verification:** Identifies risky executable and script formats (`.exe`, `.bat`, `.vbs`, `.cmd`, `.ps1`, `.scr`)
  * **Content Byte Analysis:** Reads up to the first 2,000 bytes of a file to search for embedded dangerous command strings (e.g., `powershell`, `cmd.exe`, `mimikatz`, `shellcode`, `regedit`)
* **Interactive UI Controls:**
  * Single File Scan (`filedialog.askopenfilename`)
  * Multi-File Scan (`filedialog.askopenfilenames`)
  * Whole Folder Directory Scan (`filedialog.askdirectory`)
* **Dynamic Results & Quarantine:** Real-time visual logging of threat severity levels (LOW, MEDIUM, HIGH) and automatic Quarantine list updates

---

## 🚀 How to Run

1. Ensure Python 3.x is installed on your system.
2. Run the application from your terminal or IDE:

```bash
python app.py

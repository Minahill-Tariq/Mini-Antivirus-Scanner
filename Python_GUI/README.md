# Python GUI Frontend (Tkinter)

A dark-themed desktop application built with **Python 3** and **Tkinter** that provides interactive file browsing, multi-rule threat detection, real-time reporting, and dynamic quarantine logging[cite: 1].

---

## 🔑 Default Credentials

The application includes pre-configured credentials alongside a functional user registration (Sign Up) workflow[cite: 1]:

* **Default Username:** `minahil`
* **Default Password:** `1234`

---

## 🛠️ Features & Mechanics

* **Authentication System:** Includes login validation and dynamic in-memory account creation[cite: 1].
* **Three-Tier Scanning Engine:**
  * **Filename Inspection:** Scans file basenames for high-risk malware keywords (e.g., `virus`, `hack`, `malware`, `trojan`, `rootkit`, `backdoor`)[cite: 1].
  * **Extension Verification:** Identifies risky executable and script formats (`.exe`, `.bat`, `.vbs`, `.cmd`, `.ps1`, `.scr`)[cite: 1].
  * **Content Byte Analysis:** Reads up to the first 2,000 bytes of a file to search for embedded dangerous command strings (e.g., `powershell`, `cmd.exe`, `mimikatz`, `shellcode`, `regedit`)[cite: 1].
* **Interactive UI Controls:**
  * Single File Scan (`filedialog.askopenfilename`)[cite: 1]
  * Multi-File Scan (`filedialog.askopenfilenames`)[cite: 1]
  * Whole Folder Directory Scan (`filedialog.askdirectory`)[cite: 1]
* **Dynamic Results & Quarantine:** Real-time visual logging of threat severity levels (LOW, MEDIUM, HIGH) and automatic Quarantine list updates[cite: 1].

---

## 🚀 How to Run

1. Ensure Python 3.x is installed on your system.
2. Run the application from your terminal or IDE:

```bash
python app.py

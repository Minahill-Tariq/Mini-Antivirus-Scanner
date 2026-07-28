# Mini-Antivirus-Scanner
A two-layer cybersecurity tool with an x86 Assembly backend and Python Tkinter GUI.
# Mini Antivirus Scanner

A dual-layer cybersecurity application demonstrating threat detection mechanics at both the machine instruction level (x86 Assembly) and through an interactive desktop interface (Python Tkinter).

---

## 🌟 Overview & Key Features

* **Two-Layer Architecture:** Features an independent low-level x86 Assembly (MASM) console application and a modern Python Tkinter GUI.
* **Authentication Portal:** Built-in login authentication system across both layers (Includes default access credentials: `minahil` / `1234` alongside an in-memory registration option).
* **Multi-Tier Threat Detection:**
  * **Filename Inspection:** Flags suspicious keywords (`virus`, `hack`, `malware`, `trojan`, `rootkit`, `backdoor`).
  * **Extension Verification:** Detects risky file extensions (`.exe`, `.bat`, `.vbs`, `.ps1`, `.cmd`, `.scr`).
  * **Payload / Content Analysis:** Performs byte-level analysis (first 2,000 bytes) for dangerous commands (`powershell`, `cmd.exe`, `mimikatz`, `shellcode`).
* **Persistent Quarantine Registry:** Tracks and isolates flagged files during active scan sessions.
* **Flexible Scanning Modes:** Quick Single File, Multi-file Select, and Folder Directory Scanning.

---

## 🏗️ Architecture Breakdown

| Layer | Technology | Key Capabilities |
| :--- | :--- | :--- |
| **Backend Core** | x86 Assembly (MASM) & Irvine32 | Direct memory management, custom string search routines, register preservation, and console I/O. |
| **Frontend GUI** | Python 3.x & Tkinter | Dark-themed interface, real OS file-picker integration, threat level classification (LOW, MEDIUM, HIGH), live reporting, and dynamic quarantine viewer. |

---

## 🔍 Detection Engine Logic

1. **Filename Check:** Scans file basenames for high-risk malware terminology.
2. **Extension Verification:** Blocks executable and scripting extensions.
3. **Byte Inspection (GUI Layer):** Reads raw byte data from files to identify dangerous payload strings even if the filename is disguised.

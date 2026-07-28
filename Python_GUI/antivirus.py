import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

SUSPICIOUS_STRINGS = [
    "powershell", "cmd.exe", "regedit", "keylog",
    "shellcode", "WScript", "AutoRun", "CreateRemote",
    "mimikatz", "exploit", "payload", "rootkit",
    "backdoor", "ransomware", "cryptolocker", "botnet"
]

SUSPICIOUS_FILENAMES = [
    "virus", "hack", "malware", "trojan",
    "worm", "spyware", "adware", "rootkit",
    "backdoor", "keylog", "exploit", "payload"
]

SUSPICIOUS_EXTENSIONS = [".exe", ".bat", ".vbs", ".cmd", ".ps1", ".scr"]

BG        = "#0a0a0a"
PANEL     = "#111111"
BORDER    = "#1e1e1e"
CYAN      = "#00d4ff"
GREEN     = "#00ff88"
RED       = "#ff3333"
YELLOW    = "#ffcc00"
WHITE     = "#ffffff"
GRAY      = "#888888"
DARK_RED  = "#1a0000"
DARK_GREEN= "#001a0a"

def scan_file(filepath):
    filename = os.path.basename(filepath).lower()
    ext      = os.path.splitext(filepath)[1].lower()
    threats  = []


    for kw in SUSPICIOUS_FILENAMES:
        if kw in filename:
            threats.append(f"Suspicious filename keyword: '{kw}'")

    if ext in SUSPICIOUS_EXTENSIONS:
        threats.append(f"Dangerous file extension: '{ext}'")

    try:
        with open(filepath, "rb") as f:
            raw = f.read(2000)
        try:
            content = raw.decode("utf-8", errors="ignore").lower()
        except:
            content = ""

        for s in SUSPICIOUS_STRINGS:
            if s.lower() in content:
                threats.append(f"Suspicious content found: '{s}'")
    except Exception as e:
        threats.append(f"Could not read file: {str(e)}")

    if threats:
        if len(threats) >= 3:
            level = "HIGH"
        elif len(threats) == 2:
            level = "MEDIUM"
        else:
            level = "LOW"
        return "THREAT", level, threats
    else:
        return "SAFE", None, []

class AuthWindow:
    def __init__(self, root, on_success):
        self.root       = root
        self.on_success = on_success
        self.signup_user = None
        self.signup_pass = None

        self.root.title("Mini Antivirus Scanner - Login")
        self.root.geometry("480x540")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.build_auth_menu()


    def build_auth_menu(self):
        self._clear()

        tk.Label(self.root, text="========================================",
                 fg=CYAN, bg=BG, font=("Courier", 11)).pack(pady=(30, 0))
        tk.Label(self.root, text="     MINI ANTIVIRUS SCANNER",
                 fg=CYAN, bg=BG, font=("Courier", 13, "bold")).pack()
        tk.Label(self.root, text="========================================",
                 fg=CYAN, bg=BG, font=("Courier", 11)).pack()
        tk.Label(self.root, text="WELCOME TO CYBER SECURITY PROJECT",
                 fg=WHITE, bg=BG, font=("Courier", 10)).pack(pady=(8, 30))

        frame = tk.Frame(self.root, bg=PANEL,
                         highlightbackground=CYAN, highlightthickness=1)
        frame.pack(padx=40, fill="x")

        tk.Label(frame, text="SELECT AN OPTION", fg=CYAN, bg=PANEL,
                 font=("Courier", 12, "bold")).pack(pady=(18, 16))

        tk.Button(frame, text="[ 1.  Login ]",
                  fg=WHITE, bg=PANEL,
                  font=("Courier", 12),
                  activebackground=CYAN, activeforeground=BG,
                  bd=0, cursor="hand2", pady=8,
                  command=self.build_login).pack(fill="x", padx=20, pady=6)

        tk.Button(frame, text="[ 2.  Sign Up ]",
                  fg=WHITE, bg=PANEL,
                  font=("Courier", 12),
                  activebackground=CYAN, activeforeground=BG,
                  bd=0, cursor="hand2", pady=8,
                  command=self.build_signup).pack(fill="x", padx=20, pady=(0, 20))
    def build_login(self):
        self._clear()
        self.attempts = 0

        tk.Label(self.root, text="========================================",
                 fg=CYAN, bg=BG, font=("Courier", 11)).pack(pady=(30, 0))
        tk.Label(self.root, text="     MINI ANTIVIRUS SCANNER",
                 fg=CYAN, bg=BG, font=("Courier", 13, "bold")).pack()
        tk.Label(self.root, text="========================================",
                 fg=CYAN, bg=BG, font=("Courier", 11)).pack()
        tk.Label(self.root, text="WELCOME TO CYBER SECURITY PROJECT",
                 fg=WHITE, bg=BG, font=("Courier", 10)).pack(pady=(8, 20))

        frame = tk.Frame(self.root, bg=PANEL,
                         highlightbackground=CYAN, highlightthickness=1)
        frame.pack(padx=40, fill="x")

        tk.Label(frame, text="LOGIN PORTAL", fg=CYAN, bg=PANEL,
                 font=("Courier", 12, "bold")).pack(pady=(18, 12))

        tk.Label(frame, text="Username:", fg=GRAY, bg=PANEL,
                 font=("Courier", 10), anchor="w").pack(padx=20, fill="x")
        self.user_entry = tk.Entry(frame, bg=BORDER, fg=WHITE,
                                   font=("Courier", 11),
                                   insertbackground=WHITE, bd=0,
                                   highlightbackground=CYAN,
                                   highlightthickness=1)
        self.user_entry.pack(padx=20, pady=(4, 12), fill="x", ipady=6)

        tk.Label(frame, text="Password:", fg=GRAY, bg=PANEL,
                 font=("Courier", 10), anchor="w").pack(padx=20, fill="x")
        self.pass_entry = tk.Entry(frame, bg=BORDER, fg=WHITE,
                                   font=("Courier", 11), show="*",
                                   insertbackground=WHITE, bd=0,
                                   highlightbackground=CYAN,
                                   highlightthickness=1)
        self.pass_entry.pack(padx=20, pady=(4, 16), fill="x", ipady=6)

        self.msg_label = tk.Label(frame, text="", bg=PANEL,
                                  font=("Courier", 10))
        self.msg_label.pack(pady=(0, 8))

        tk.Button(frame, text="[ LOGIN ]",
                  fg=CYAN, bg=PANEL,
                  font=("Courier", 12, "bold"),
                  activebackground=CYAN, activeforeground=BG,
                  bd=0, cursor="hand2",
                  command=self.attempt_login).pack(pady=(0, 10))

        tk.Button(frame, text="< Back",
                  fg=GRAY, bg=PANEL,
                  font=("Courier", 9),
                  activebackground=BORDER, activeforeground=WHITE,
                  bd=0, cursor="hand2",
                  command=self.build_auth_menu).pack(pady=(0, 16))

        self.pass_entry.bind("<Return>", lambda e: self.attempt_login())
        self.user_entry.focus()

    def attempt_login(self):
        u = self.user_entry.get().strip()
        p = self.pass_entry.get().strip()

   
        if u == "minahil" and p == "1234":
            self.msg_label.config(text="Access Granted!", fg=GREEN)
            self.root.after(800, self.on_success)
            return

        if self.signup_user and u == self.signup_user and p == self.signup_pass:
            self.msg_label.config(text="Access Granted!", fg=GREEN)
            self.root.after(800, self.on_success)
            return

        self.attempts += 1
        self.msg_label.config(
            text=f"Invalid Credentials! Try Again. ({self.attempts})",
            fg=RED)
        self.pass_entry.delete(0, "end")

    
    def build_signup(self):
        self._clear()

        tk.Label(self.root, text="========================================",
                 fg=CYAN, bg=BG, font=("Courier", 11)).pack(pady=(30, 0))
        tk.Label(self.root, text="     MINI ANTIVIRUS SCANNER",
                 fg=CYAN, bg=BG, font=("Courier", 13, "bold")).pack()
        tk.Label(self.root, text="========================================",
                 fg=CYAN, bg=BG, font=("Courier", 11)).pack()
        tk.Label(self.root, text="WELCOME TO CYBER SECURITY PROJECT",
                 fg=WHITE, bg=BG, font=("Courier", 10)).pack(pady=(8, 20))

        frame = tk.Frame(self.root, bg=PANEL,
                         highlightbackground=CYAN, highlightthickness=1)
        frame.pack(padx=40, fill="x")

        tk.Label(frame, text="SIGN UP", fg=CYAN, bg=PANEL,
                 font=("Courier", 12, "bold")).pack(pady=(18, 12))

        tk.Label(frame, text="Choose a Username:", fg=GRAY, bg=PANEL,
                 font=("Courier", 10), anchor="w").pack(padx=20, fill="x")
        self.new_user_entry = tk.Entry(frame, bg=BORDER, fg=WHITE,
                                       font=("Courier", 11),
                                       insertbackground=WHITE, bd=0,
                                       highlightbackground=CYAN,
                                       highlightthickness=1)
        self.new_user_entry.pack(padx=20, pady=(4, 12), fill="x", ipady=6)

        tk.Label(frame, text="Choose a Password:", fg=GRAY, bg=PANEL,
                 font=("Courier", 10), anchor="w").pack(padx=20, fill="x")
        self.new_pass_entry = tk.Entry(frame, bg=BORDER, fg=WHITE,
                                       font=("Courier", 11), show="*",
                                       insertbackground=WHITE, bd=0,
                                       highlightbackground=CYAN,
                                       highlightthickness=1)
        self.new_pass_entry.pack(padx=20, pady=(4, 16), fill="x", ipady=6)

        self.signup_msg = tk.Label(frame, text="", bg=PANEL,
                                   font=("Courier", 10))
        self.signup_msg.pack(pady=(0, 8))

        tk.Button(frame, text="[ SIGN UP ]",
                  fg=CYAN, bg=PANEL,
                  font=("Courier", 12, "bold"),
                  activebackground=CYAN, activeforeground=BG,
                  bd=0, cursor="hand2",
                  command=self.attempt_signup).pack(pady=(0, 10))

        tk.Button(frame, text="< Back",
                  fg=GRAY, bg=PANEL,
                  font=("Courier", 9),
                  activebackground=BORDER, activeforeground=WHITE,
                  bd=0, cursor="hand2",
                  command=self.build_auth_menu).pack(pady=(0, 16))

        self.new_pass_entry.bind("<Return>", lambda e: self.attempt_signup())
        self.new_user_entry.focus()

    def attempt_signup(self):
        u = self.new_user_entry.get().strip()
        p = self.new_pass_entry.get().strip()
        if not u:
            self.signup_msg.config(text="Username cannot be empty!", fg=RED)
            return

        if not p:
            self.signup_msg.config(text="Password cannot be empty!", fg=RED)
            return
        self.signup_user = u
        self.signup_pass = p
        self.signup_msg.config(text="Account created! Please login now.", fg=GREEN)
        self.root.after(1200, self.build_login)
    def _clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

class ScannerWindow:
    def __init__(self, root):
        self.root        = root
        self.quarantine  = []
        self.total_scanned = 0
        self.total_threats = 0
        self.total_safe    = 0

        self.root.title("Mini Antivirus Scanner")
        self.root.geometry("860x680")
        self.root.configure(bg=BG)
        self.root.resizable(True, True)

        self.build()

    def build(self):

        top = tk.Frame(self.root, bg=BG)
        top.pack(fill="x", padx=20, pady=(16,0))

        tk.Label(top, text="========================================",
                 fg=CYAN, bg=BG, font=("Courier", 12)).pack()
        tk.Label(top, text="       MINI ANTIVIRUS SCANNER",
                 fg=CYAN, bg=BG, font=("Courier", 14, "bold")).pack()
        tk.Label(top, text="========================================",
                 fg=CYAN, bg=BG, font=("Courier", 12)).pack()

        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=20, pady=12)

  
        left = tk.Frame(body, bg=BG)
        left.pack(side="left", fill="both", expand=True)


        btn_frame = tk.Frame(left, bg=PANEL,
                             highlightbackground=BORDER,
                             highlightthickness=1)
        btn_frame.pack(fill="x", pady=(0,10))

        tk.Label(btn_frame, text="SCAN OPTIONS", fg=CYAN, bg=PANEL,
                 font=("Courier", 11, "bold")).pack(pady=(10,8))

        b1 = tk.Button(btn_frame,
                       text="[ Browse & Scan Single File ]",
                       fg=WHITE, bg=PANEL,
                       font=("Courier", 10),
                       activebackground=CYAN,
                       activeforeground=BG,
                       bd=0, cursor="hand2",
                       pady=6,
                       command=self.browse_single)
        b1.pack(fill="x", padx=16, pady=4)

        b2 = tk.Button(btn_frame,
                       text="[ Browse & Scan Multiple Files ]",
                       fg=WHITE, bg=PANEL,
                       font=("Courier", 10),
                       activebackground=CYAN,
                       activeforeground=BG,
                       bd=0, cursor="hand2",
                       pady=6,
                       command=self.browse_multiple)
        b2.pack(fill="x", padx=16, pady=4)

        b3 = tk.Button(btn_frame,
                       text="[ Scan Entire Folder ]",
                       fg=WHITE, bg=PANEL,
                       font=("Courier", 10),
                       activebackground=CYAN,
                       activeforeground=BG,
                       bd=0, cursor="hand2",
                       pady=6,
                       command=self.browse_folder)
        b3.pack(fill="x", padx=16, pady=(4,14))


        res_label = tk.Label(left, text="SCAN RESULTS",
                             fg=CYAN, bg=BG,
                             font=("Courier", 11, "bold"),
                             anchor="w")
        res_label.pack(fill="x", pady=(4,4))

        res_frame = tk.Frame(left, bg=PANEL,
                             highlightbackground=BORDER,
                             highlightthickness=1)
        res_frame.pack(fill="both", expand=True)

        self.results_text = tk.Text(res_frame, bg=PANEL, fg=WHITE,
                                    font=("Courier", 10),
                                    bd=0, wrap="word",
                                    state="disabled",
                                    insertbackground=WHITE)
        scroll = tk.Scrollbar(res_frame, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.results_text.pack(fill="both", expand=True, padx=8, pady=8)

        self.results_text.tag_config("safe",    foreground=GREEN)
        self.results_text.tag_config("threat",  foreground=RED)
        self.results_text.tag_config("warn",    foreground=YELLOW)
        self.results_text.tag_config("info",    foreground=CYAN)
        self.results_text.tag_config("gray",    foreground=GRAY)
        self.results_text.tag_config("white",   foreground=WHITE)

        right = tk.Frame(body, bg=BG, width=240)
        right.pack(side="right", fill="y", padx=(14,0))
        right.pack_propagate(False)

        report = tk.Frame(right, bg=PANEL,
                          highlightbackground=BORDER,
                          highlightthickness=1)
        report.pack(fill="x", pady=(0,10))

        tk.Label(report, text="SCAN REPORT", fg=CYAN, bg=PANEL,
                 font=("Courier", 11, "bold")).pack(pady=(10,8))

        self.lbl_scanned = tk.Label(report,
                                    text="Files Scanned : 0",
                                    fg=WHITE, bg=PANEL,
                                    font=("Courier", 10))
        self.lbl_scanned.pack(anchor="w", padx=14)

        self.lbl_threats = tk.Label(report,
                                    text="Threats Found : 0",
                                    fg=RED, bg=PANEL,
                                    font=("Courier", 10))
        self.lbl_threats.pack(anchor="w", padx=14)

        self.lbl_safe = tk.Label(report,
                                 text="Safe Files    : 0",
                                 fg=GREEN, bg=PANEL,
                                 font=("Courier", 10))
        self.lbl_safe.pack(anchor="w", padx=14, pady=(0,12))

        tk.Button(report, text="[ Clear Report ]",
                  fg=GRAY, bg=PANEL,
                  font=("Courier", 9),
                  activebackground=BORDER,
                  activeforeground=WHITE,
                  bd=0, cursor="hand2",
                  command=self.clear_all).pack(pady=(0,10))
        tk.Label(right, text="QUARANTINE",
                 fg=RED, bg=BG,
                 font=("Courier", 11, "bold"),
                 anchor="w").pack(fill="x", pady=(4,4))

        q_frame = tk.Frame(right, bg=PANEL,
                           highlightbackground=BORDER,
                           highlightthickness=1)
        q_frame.pack(fill="both", expand=True)

        self.q_text = tk.Text(q_frame, bg=PANEL, fg=RED,
                              font=("Courier", 9),
                              bd=0, wrap="word",
                              state="disabled")
        qs = tk.Scrollbar(q_frame, command=self.q_text.yview)
        self.q_text.configure(yscrollcommand=qs.set)
        qs.pack(side="right", fill="y")
        self.q_text.pack(fill="both", expand=True, padx=6, pady=6)

        self.status = tk.Label(self.root,
                               text="Ready. Choose a scan option above.",
                               fg=GRAY, bg=BORDER,
                               font=("Courier", 9),
                               anchor="w")
        self.status.pack(fill="x", side="bottom", ipady=4, padx=8)
    def browse_single(self):
        path = filedialog.askopenfilename(
            title="Select a file to scan",
            filetypes=[("All Files", "*.*"),
                       ("PDF Files", "*.pdf"),
                       ("Word Files", "*.docx"),
                       ("Executables", "*.exe"),
                       ("Text Files", "*.txt")])
        if path:
            self.run_scan([path])

    def browse_multiple(self):
        paths = filedialog.askopenfilenames(
            title="Select files to scan",
            filetypes=[("All Files", "*.*")])
        if paths:
            self.run_scan(list(paths))

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select folder to scan")
        if folder:
            files = []
            for f in os.listdir(folder):
                full = os.path.join(folder, f)
                if os.path.isfile(full):
                    files.append(full)
            if files:
                self.run_scan(files)
            else:
                messagebox.showinfo("Empty", "No files found in folder.")

    def run_scan(self, filepaths):
        self.set_status(f"Scanning {len(filepaths)} file(s)...")
        self.write_result("\n", "white")
        self.write_result("Scanning Files...\n", "info")
        self.write_result("----------------------------------------\n", "gray")

        for fp in filepaths:
            name   = os.path.basename(fp)
            status, level, reasons = scan_file(fp)

            self.write_result(f"{name}\n", "white")
            self.total_scanned += 1

            if status == "SAFE":
                self.total_safe += 1
                self.write_result("  --> SAFE FILE\n", "safe")
            else:
                self.total_threats += 1
                self.write_result("  --> THREAT DETECTED\n", "threat")
                self.write_result(f"  Threat Level : {level}\n", "warn")
                for r in reasons:
                    self.write_result(f"  * {r}\n", "warn")
                self.quarantine.append(name)
                self.update_quarantine()

            self.write_result("----------------------------------------\n",
                              "gray")

        self.update_report()
        self.set_status(
            f"Scan complete. {self.total_scanned} scanned, "
            f"{self.total_threats} threats, {self.total_safe} safe.")
    def write_result(self, text, tag="white"):
        self.results_text.configure(state="normal")
        self.results_text.insert("end", text, tag)
        self.results_text.see("end")
        self.results_text.configure(state="disabled")

    def update_report(self):
        self.lbl_scanned.config(
            text=f"Files Scanned : {self.total_scanned}")
        self.lbl_threats.config(
            text=f"Threats Found : {self.total_threats}")
        self.lbl_safe.config(
            text=f"Safe Files    : {self.total_safe}")

    def update_quarantine(self):
        self.q_text.configure(state="normal")
        self.q_text.delete("1.0", "end")
        for name in self.quarantine:
            self.q_text.insert("end", f"{name}\n")
        self.q_text.configure(state="disabled")

    def set_status(self, msg):
        self.status.config(text=msg)
        self.root.update()

    def clear_all(self):
        self.total_scanned = 0
        self.total_threats = 0
        self.total_safe    = 0
        self.quarantine    = []
        self.results_text.configure(state="normal")
        self.results_text.delete("1.0", "end")
        self.results_text.configure(state="disabled")
        self.q_text.configure(state="normal")
        self.q_text.delete("1.0", "end")
        self.q_text.configure(state="disabled")
        self.update_report()
        self.set_status("Cleared. Ready for new scan.")

def launch_scanner():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("860x680")
    ScannerWindow(root)

root = tk.Tk()
AuthWindow(root, on_success=launch_scanner)
root.mainloop()

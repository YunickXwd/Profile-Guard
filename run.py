import platform
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print("""
╔══════════════════════════════════════════════╗
║          🛡️  PROFILE GUARD TOOL LAUNCHER 🛡️        ║
╠══════════════════════════════════════════════╣
║ Author   : YunickXwd                         ║
║ GitHub   : https://github.com/YunickXwd      ║
║ Version  : 1.0                               ║
╚══════════════════════════════════════════════╝
""")

def check_architecture():
    arch = platform.machine()
    if 'aarch64' in arch or 'arm64' in arch:
        return '64-bit'
    elif 'arm' in arch or 'i686' in arch:
        return '32-bit'
    else:
        return 'unknown'

def run_main_module():
    try:
        import main  # main.cpython-312.so (generated from Cython)
    except ImportError as e:
        print("[!] Failed to load the module:", e)

def main():
    banner()
    print("[*] Checking device architecture...")
    time.sleep(1)

    arch = check_architecture()
    print(f"[✔] Detected architecture: {arch}")

    if arch == '64-bit':
        print("\n[+] Device supported! Launching tool...\n")
        time.sleep(1)
        run_main_module()
    elif arch == '32-bit':
        print("\n[❌] Sorry bro, 32-bit devices are not supported 😞")
    else:
        print("\n[❗] Unknown device architecture. Cannot continue.")

if __name__ == "__main__":
    main()

import os
import sys
import subprocess
import venv
from pathlib import Path

common_packages = [
    "psutil>=5.9.4",
    "beautifulsoup4>=4.11.1",
    "colorama>=0.4.6",
    "requests==2.28.1",
    "pytelegrambotapi==4.8.0",
    "pillow>=9.3.0",
    "aiohttp==3.8.3",
    "requests_toolbelt==0.10.1",
    "pystray>=0.19.5",
]

venv_dir = Path(__file__).parent / "venv"

def create_venv():
    if not venv_dir.exists():
        print("[+] Создаю виртуальное окружение...")
        venv.create(venv_dir, with_pip=True)
    else:
        print("[=] Виртуальное окружение уже существует.")

def get_pip_path():
    if os.name == "nt":
        return venv_dir / "Scripts" / "pip.exe"
    else:
        return venv_dir / "bin" / "pip"

def install_packages(packages):
    pip_path = str(get_pip_path())
    # Upgrade pip first to improve wheel resolution
    try:
        subprocess.check_call([pip_path, "install", "--upgrade", "pip"])
    except Exception:
        pass
    for pkg in packages:
        print(f"[+] Устанавливаю {pkg}...")
        subprocess.check_call([pip_path, "install", "-U", pkg])

if __name__ == "__main__":
    create_venv()
    install_packages(common_packages)
    print("\n✅ Все пакеты установлены в venv:", venv_dir)

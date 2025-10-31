import sys

REQUIRED_MODULES = [
    "psutil",
    "bs4",
    "colorama",
    "requests",
    "telebot",
    "PIL",
    "aiohttp",
    "requests_toolbelt",
    "pystray",
]

def main() -> int:
    missing = []
    for module_name in REQUIRED_MODULES:
        try:
            __import__(module_name)
        except Exception:
            missing.append(module_name)
    if missing:
        print("Missing modules:", ", ".join(missing))
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())






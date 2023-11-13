import os
import json
import argparse

def find_executable_path(app_path):
    for root, dirs, files in os.walk(app_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.access(file_path, os.X_OK) and '.' not in file and "chrome" not in file:
                return file_path

def find_icon_path(app_path):
    for root, dirs, files in os.walk(app_path):
        for file in files:
            if file.endswith(".png") or file.endswith(".ico"):
                return os.path.join(root, file)

def find_name(app_path):
    nativefier_json_path = os.path.join(app_path, "resources/app/nativefier.json")
    if os.path.exists(nativefier_json_path):
        with open(nativefier_json_path, "r") as json_file:
            data = json.load(json_file)
            return data.get("name", "MyApp")

def create_desktop_entry(app_path):
    app_exec = find_executable_path(app_path)
    app_name = find_name(app_path)
    app_icon = find_icon_path(app_path)

    if not app_exec or not app_name:
        print("Error: Unable to determine executable path or app name.")
        return

    desktop_entry_file = f"{app_name.lower().replace(' ', '_')}.desktop"
    desktop_entry_path = os.path.join(os.path.expanduser("~/.local/share/applications"), desktop_entry_file)

    with open(desktop_entry_path, 'w') as desktop_file:
        desktop_file.write(f"[Desktop Entry]\n")
        desktop_file.write(f"Type=Application\n")
        desktop_file.write(f"Name={app_name}\n")
        desktop_file.write(f"Exec={app_exec}\n")
        desktop_file.write(f"Categories=Development;Network;WebBrowser\n")
        if app_icon:
            desktop_file.write(f"Icon={app_icon}\n")
        desktop_file.write(f"Terminal=false\n")

    print(f"Desktop entry file created: {desktop_entry_path}")

def main():
    parser = argparse.ArgumentParser(description="Create a desktop entry for a Nativefier-generated web app.")
    parser.add_argument("app_path", help="Path to the directory of the Nativefier-generated web app")
    args = parser.parse_args()

    create_desktop_entry(args.app_path)

if __name__ == "__main__":
    main()


# 😴 Nativefier DE 

The `Nativefier_DE` is a Python script that simplifies the process of creating desktop entry files for web applications generated using `Nativefier`. This allows for seamless integration of web apps into the Linux desktop environment.s

## 😈 Features

- Automatically `detects` and `sets` executable `paths`.
- Extracts application `name` and `icon` information from `Nativefier-generated content`.
- Creates desktop entry files compatible with `Linux desktop environments`.

## 👻👻 Prerequisites

- Python 3.x
- Nativefier (install with `npm install -g nativefier`, `snap install nativefier`)

## 🤔 Usage

1. Generate a web application using `Nativefier`.
   ```bash
   nativefier "yourwebapp.com"
   ```

2. Run the script, providing the `path` to the directory of the `generated web app`.
   ```bash
   python3 build.py /path/to/your/web-app-directory
   ```

3. `Refresh` your desktop environment or `restart` to see the newly created desktop entry.

## Options

- The script automatically determines the `executable path` and extracts application `name` and `icon` information. However, you can customize the behavior by editing the script as needed.

### If you found this `useful` consider leaving a star and invite your `friends`

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or suggest improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

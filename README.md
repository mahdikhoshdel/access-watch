# Access Watch

**Access Watch** is a Python script designed to retrieve and display file access information, such as last access time and file ownership details, on both Linux and Windows systems. The script utilizes OS-specific modules to gather this information, making it versatile and suitable for cross-platform environments.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Examples](#examples)
7. [Contributing](#contributing)
8. [License](#license)

## Features

- Retrieve and display the last access time of a file.
- Display the file owner's user ID (UID) and group ID (GID).
- Convert UID to username and GID to group name (Linux only).
- Cross-platform support: Works on both Linux and Windows.

## Requirements

- Python 3.x
- Linux: `pwd` and `grp` modules (standard in Python on Unix-like systems)
- Windows: `pywin32` package for Windows-specific functionalities (only if using the Windows module)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mahdikhoshdel/access-watch.git
   cd access-watch
   ```

2. **Install Required Packages:**

   - For Linux: No additional installation is required.
   - For Windows (if you plan to test on Windows):

     ```bash
     pip install pywin32
     ```

## Usage

1. **Run the Script:**

   Use the following command to run the script, specifying the file path you want to check:

   ```bash
   python file_access_info.py /path/to/your/file
   ```

2. **Command-Line Argument:**

   The script accepts a file path as a command-line argument:

   ```bash
   python file_access_info.py /path/to/your/file
   ```

   Example for Linux:

   ```bash
   python file_access_info.py /home/user/documents/example.txt
   ```

   Example for Windows:

   ```bash
   python file_access_info.py C:\Users\User\Documents\example.txt
   ```

## Project Structure

```
access-watch/
├── README.md
└── source/
   ├── main.py
   ├── linux.py
   └── windows.py
```

- `main.py`: Main script to run the project.
- `linux.py`: Module containing Linux-specific file access logic.
- `windows.py`: Module containing Windows-specific file access logic.

## Examples

To check the access information of a file on a Linux system:

```bash
python main.py /home/user/sample.txt
python main.py /home/user/sample/directory/
```

Output in Linux:

```
Last Access Time: Wed Aug 23 13:00:00 2023
File Owner UID: 1000 (Username: user)
File Owner GID: 1000 (Group Name: usergroup)
```

Output in Windows:

```
Last access time : Sun Aug 25 11:13:30 2024
Last access SID : SID
ID/UserName (Account Type: account-type)
```


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.




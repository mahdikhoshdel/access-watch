import os
import argparse

if os.name == "posix":
    from linux import LinuxFileAccessInfo
elif os.name == "nt":
    from windows import WindowsFileAccessInfo

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get file access information")
    parser.add_argument("file_path", help="Path to the file")
    args = parser.parse_args()

    if os.name == "posix":
        file_info = LinuxFileAccessInfo(args.file_path)
    elif os.name == "nt":
        file_info = WindowsFileAccessInfo(args.file_path)
    else:
        print("Your OS is not supported by this program")
        exit(1)
    
    file_info.review()

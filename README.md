# File Access Information Tool  

## Overview  
The File Access Information Tool is a Python utility that retrieves and displays file access information. It provides details such as the last access time and the file owner information for specified files. This tool is particularly useful for system administrators and users who want to understand file access patterns and ownership on Windows systems.  

## Features  
- Retrieve the last access time of a specified file.  
- Identify the owner of a file by its Security Identifier (SID).  
- Convert SID to a human-readable username format.  
- Simple command-line interface for ease of use.  

## Requirements  
- Python 3.x  
- `pywin32` library (for Windows API access)  

## Installation  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/yourusername/file-access-info-tool.git  
   cd file-access-info-tool

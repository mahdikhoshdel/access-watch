# Access Watch

**Access Watch** is a Python script designed to retrieve and display file access information, such as last access time and file ownership details, on both Linux and Windows systems. The script utilizes OS-specific modules to gather this information, making it versatile and suitable for cross-platform environments.


## Features

- Retrieve and display the last access time of a file.
- Display the file owner's user ID and group ID
- Convert user ID to username and group ID to group name.
- Cross-platform support: Works on both Linux and Windows.


## LinuxAccessWatch  

The `LinuxAccessWatch` class is designed to monitor and retrieve file information related to user access in a Linux environment. It provides methods to obtain metadata such as the last access time, owner UID, owner GID, owner username, and owner group name of a specified file or directory.  

#### Methods  

- **`get_file_stats() -> None`**: Gathers file statistics including last access time, owner UID, and owner GID.  
- **`get_owner_uid() -> Optional[int]`**: Retrieves the user ID (UID) of the file owner.  
- **`get_owner_gid() -> Optional[int]`**: Retrieves the group ID (GID) of the file owner.  
- **`uid_to_username() -> str`**: Converts the owner UID to a human-readable username.  
- **`gid_to_groupname() -> str`**: Converts the owner GID to a human-readable group name.  
- **`get_last_access_time() -> Optional[str]`**: Returns the last access time of the file in a human-readable format.
- **`get_username() -> str`**: Retrieves the username of the file owner.  
- **`get_groupname() -> str`**: Retrieves the group name of the file owner.  
 

#### Usage  

```python
from accesswatch.linux import LinuxAccessWatch

access_watch = LinuxAccessWatch("/path/to/file_or/directory")
last_access_time = access_watch.get_last_access_time()
# Sat Sep 21 10:48:05 2024
owner_uid = access_watch.get_owner_uid()
# id
owner_gid = access_watch.get_owner_gid()
# id
username = access_watch.get_username()
# username
groupname = access_watch.get_groupname()
# usergroup
```

## WindowsAccessWatch
`WindowsAccessWatch` is a class designed to monitor and retrieve information about file access on Windows systems. It tracks the last access time of a file, retrieves the owner Security Identifier (SID), and converts this SID into a human-readable account name, domain name, and account type.


#### Methods
- **`__init__(file_path)`**: Initializes the `WindowsAccessWatch` object with the file path and retrieves the owner SID.
- **`set_owner_sid()`**: Sets the owner SID for the specified file or directory.
- **`get_file_stats()`**: Retrieves the last access time and owner SID of the file.
- **`get_last_access_time()`**: Returns the last access time in a human-readable format.
- **`get_owner_sid()`**: Returns the owner SID of the file.
- **`get_owner_sid_string()`**: Returns the owner SID as a string in a human-readable format.
- **`sid_to_username_info(sid)`**: Converts a given SID to a username, domain name, and account type.
- **`user_access_info()`**: Retrieves the account name, domain name, and account type for the file owner.

#### Usage

```python
from accesswatch.windows import WindowsAccessWatch

access_watcher = WindowsAccessWatch("/path/to/file_or/directory")
last_access_time = access_watcher.get_last_access_time()        
owner_sid = access_watcher.get_owner_sid_string()
account_name, domain_name, account_type = access_watcher.user_access_info() 
```


## Contributing

Contributions are welcome!

Github:  https://github.com/mahdikhoshdel/accesswatch.git

Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.




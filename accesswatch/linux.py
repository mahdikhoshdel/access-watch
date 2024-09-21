"""
Linux Access watch:
Monitoring

- Last Access Time
- Owner UID
- Owner GID
- Owner Username
- Owner Group Name

that was used for the most recent access to a file or directory.
"""

import os  
import pwd  
import grp  
import time  
from typing import Optional  


class LinuxAccessWatch:
    """
    LinuxAccessWatch Class  

    The LinuxAccessWatch class is designed to monitor and retrieve file information  
    related to user access in a Linux environment. It provides methods to obtain  
    metadata such as the last access time, owner UID, owner GID, owner username,  
    and owner group name of a specified file or directory.  

    Methods:
        __init__(file_path: str) -> None:   
            Initializes the LinuxAccessWatch instance with the path to the file or directory.  
            
        get_file_stats() -> None:  
            Gathers file statistics including last access time, owner UID, and owner GID.  
            
        get_owner_uid() -> Optional[int]:  
            Retrieves the user ID (UID) of the file owner.  
            
        get_owner_gid() -> Optional[int]:  
            Retrieves the group ID (GID) of the file owner.  
            
        uid_to_username() -> str:  
            Converts the owner UID to a human-readable username.  
            
        gid_to_groupname() -> str:  
            Converts the owner GID to a human-readable group name.  
            
        get_last_access_time() -> Optional[str]:  
            Returns the last access time of the file in a human-readable format.  
            
        get_username() -> str:  
            Retrieves the username of the file owner.  
        
        get_groupname() -> str:  
            Retrieves the group name of the file owner.  

    Usage:
        To use the LinuxAccessWatch class, instantiate it with a file path, and   
        call its methods to retrieve various access-related information.  

        Example:
            access_watch = LinuxAccessWatch("/path/to/file_or/directory")  
            last_access_time = access_watch.get_last_access_time()  
            owner_uid = access_watch.get_owner_uid()  
            username = access_watch.get_username()  
        
    Exceptions:
        - FileNotFoundError: Raised when the specified file does not exist.  
        - KeyError: Raised when the UID or GID does not exist in the system.  
        - ValueError: Raised when the UID or GID is None.  
        - Exception: A generic exception that can be raised for miscellaneous errors.  
    """
    def __init__(self, file_path: str) -> None:  
        """  
        Initialize the LinuxAccessWatch instance.  

        Args:  
            file_path (str): The path to the file or directory to monitor.  

        This constructor sets the file path and retrieves the file statistics,  
        including the last access time, owner UID, and owner GID.  
        """  
        self.file_path: str = file_path  
        self.last_access_time: Optional[float] = None  
        self.owner_uid: Optional[int] = None  
        self.owner_gid: Optional[int] = None  
        self.get_file_stats()  

    def get_file_stats(self) -> None:  
        """  
        Retrieve and set the last access time, owner UID, and owner GID of the file.  

        This method attempts to gather file statistics using the `os.stat` function.  
        If the file does not exist or an error occurs during the retrieval,   
        it raises an appropriate exception.  

        Raises:  
            FileNotFoundError: If the specified file does not exist.  
            Exception: If an error occurs while retrieving file statistics.  
        """  
        try:  
            stat_info = os.stat(self.file_path)  
            self.last_access_time = stat_info.st_atime  
            self.owner_uid = stat_info.st_uid  
            self.owner_gid = stat_info.st_gid  
        except FileNotFoundError:  
            raise FileNotFoundError("File not found.")  
        except Exception as e:  
            raise Exception(f"An error occurred: {e}")  

    def get_owner_uid(self) -> Optional[int]:  
        """  
        Get the owner UID of the file.  

        Returns:  
            Optional[int]: The user ID (UID) of the file owner, or None if not set.  
        """  
        return self.owner_uid  

    def get_owner_gid(self) -> Optional[int]:  
        """  
        Get the owner GID of the file.  

        Returns:  
            Optional[int]: The group ID (GID) of the file owner, or None if not set.  
        """  
        return self.owner_gid  

    def uid_to_username(self) -> str:  
        """  
        Convert the owner UID to a human-readable username.  

        Returns:  
            str: The username associated with the owner UID.  

        Raises:  
            ValueError: If the owner UID is None.  
            KeyError: If the UID does not exist in the system.  
        """  
        try:  
            uid = self.get_owner_uid()  
            if uid is not None:  
                user_info = pwd.getpwuid(uid)  
                return user_info.pw_name  
            raise ValueError("Owner UID is None.")  
        except KeyError as error:  
            raise KeyError(f"UID {self.owner_uid} not found: {error}")  

    def gid_to_groupname(self) -> str:  
        """  
        Convert the owner GID to a human-readable group name.  

        Returns:  
            str: The group name associated with the owner GID.  

        Raises:  
            ValueError: If the owner GID is None.  
            KeyError: If the GID does not exist in the system.  
        """  
        try:  
            gid = self.get_owner_gid()  
            if gid is not None:  
                group_info = grp.getgrgid(gid)  
                return group_info.gr_name  
            raise ValueError("Owner GID is None.")  
        except KeyError as error:  
            raise KeyError(f"GID {self.owner_gid} not found: {error}")  

    def get_last_access_time(self) -> Optional[str]:  
        """  
        Get the last access time of the file in a human-readable format.  

        Returns:  
            Optional[str]: The last access time as a formatted string, or None if not set.  
        """  
        if self.last_access_time is not None:  
            return time.ctime(self.last_access_time)  
        return None  

    def get_username(self) -> str:  
        """  
        Retrieve the username of the file owner.  

        Returns:  
            str: The username of the owner.  
        """  
        return self.uid_to_username()  
    
    def get_groupname(self) -> str:  
        """  
        Retrieve the group name of the file owner.  

        Returns:  
            str: The group name of the owner.  
        """  
        return self.gid_to_groupname()  

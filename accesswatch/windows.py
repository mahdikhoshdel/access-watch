"""
Windows Access watch:
Monitoring

- last access time,
- account name,
- account type
- security id (sid)

that was used for the most recent access to a file or directory.
"""
import os  
import win32security  
import time
from typing import Optional, Tuple


class WindowsAccessWatch:
    """ 
    A class to monitor and retrieve information about file access on Windows systems.  

    This class provides functionalities to track the last access time of a file,  
    retrieve the owner Security Identifier (SID), and convert this SID into a   
    human-readable account name, domain name, and account type.  

    Attributes:  
        - file_path (str): The path to the file or directory being monitored.  
        - last_access_time (float): The last access time of the file (as a timestamp).  
        - owner_sid (SID): The Security Identifier of the file owner.  

    Methods:  
        - __init__(file_path): Initializes the WindowsAccessWatch object with the file path and retrieves the owner SID.  
        - _set_owner_sid(): Sets the owner SID for the specified file or directory.  
        - _get_file_stats(): Retrieves the last access time and owner SID of the file.  
        - last_access_time(): Returns the last access time in a human-readable format.  
        - _get_owner_sid(): Returns the owner SID of the file.  
        - owner_id(): Returns the owner SID as a string in a human-readable format.  
        - _sid_to_username_info(sid): Converts a given SID to a username, domain name, and account type.  
        - user_access_info(): Retrieves the account name, domain name, and account type for the file owner.  
    """ 
    def __init__(self, file_path: str) -> None:  
        self.file_path: str = file_path  
        self.last_access_time: Optional[float] = None  
        self.owner_sid: Optional[str] = None  
        self._set_owner_sid()  

    def _set_owner_sid(self) -> None:  
        """Just get and set owner SID that accessed that specific file or directory."""  
        try:
            self.owner_sid = win32security.GetFileSecurity(
                self.file_path,
                win32security.OWNER_SECURITY_INFORMATION
            ).GetSecurityDescriptorOwner()  
        except:
            raise FileNotFoundError("Invalid file path")

    def _get_file_stats(self) -> bool:  
        """Get last access time and file owner SID."""  
        try:  
            stat_info = os.stat(self.file_path)  
            self.last_access_time = stat_info.st_atime  
        except FileNotFoundError:  
            return False   
        except Exception as e:  
            print(f"An error occurred: {e}")  
            return False  
        return True  

    def last_access_time(self) -> str:  
        """  
        Return last access time in a human-readable format.  
        
        Args:  
            None  

        Returns:  
            str: time  
                 example: Thu Sep  5 15:18:36 2024  
        """  
        if not self.last_access_time:  
            self._get_file_stats()  
        return time.ctime(self.last_access_time)

    def _get_owner_sid(self) -> Optional[str]:  
        """Return the owner SID."""  
        return self.owner_sid if self.owner_sid is not None else None  
    
    def owner_sid(self) -> Optional[str]:  
        """Return the owner SID as a string in human-readable format."""  
        if self.owner_sid is not None:   
            return win32security.ConvertSidToStringSid(self.owner_sid)  
        return None  

    def _sid_to_username_info(self, sid: str) -> Tuple[str, str, str]:  
        """  
        Use access_user_info() to have user info without set SID  
        Convert SID to username.  

        Args:  
            sid (str): The SID to convert.  

        Returns:  
            tuple: (Account Name (str), Domain Name (str), Account Type (str))  
        """  
        try:  
            account_name, domain_name, account_type = win32security.LookupAccountSid(None, sid)  
            return account_name, domain_name, account_type   
        except Exception as error:  
            raise RuntimeError(f"Error retrieving user info from SID: {error}")  
        
    def user_access_info(self) -> Tuple[str, str, str]:  
        """  
        Convert SID to username.  

        Args:  
            None  
        
        Returns:  
            tuple: (Account Name (str), Domain Name (str), Account Type (str))
        
        (Account Type == 1) : Admin Group
        (Account Type == 2) : Standard Group(limited)
        """  
        sid = self._get_owner_sid()  
        if sid is not None:  
            return self._sid_to_username_info(sid)  
        raise ValueError("Owner SID is None; cannot retrieve user access information.")  
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
        - set_owner_sid(): Sets the owner SID for the specified file or directory.  
        - get_file_stats(): Retrieves the last access time and owner SID of the file.  
        - get_last_access_time(): Returns the last access time in a human-readable format.  
        - get_owner_sid(): Returns the owner SID of the file.  
        - get_owner_sid_string(): Returns the owner SID as a string in a human-readable format.  
        - sid_to_username_info(sid): Converts a given SID to a username, domain name, and account type.  
        - access_info(): Retrieves the account name, domain name, and account type for the file owner.  
    """ 
    def __init__(self, file_path):  
        self.file_path = file_path  
        self.last_access_time = None  
        self.set_owner_sid()  
       
    def set_owner_sid(self):
        """Just get and set owner sid that accessed to that specific file or directory"""
        self.owner_sid = win32security.GetFileSecurity(  
                self.file_path,   
                win32security.OWNER_SECURITY_INFORMATION  
            ).GetSecurityDescriptorOwner()

    def get_file_stats(self):  
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

    def get_last_access_time(self):  
        """
        Return last access time in a human-readable format
        Args:
            None

        Returns:
            str: time
                example: Thu Sep  5 15:18:36 2024
        """  
        if not self.last_access_time:  
            self.get_file_stats()
            return time.ctime(self.last_access_time)
        raise FileNotFoundError 

    def get_owner_sid(self):  
        """Return the owner SID."""  
        if self.owner_sid is not None: 
            return self.owner_sid 
        return None
    
    def get_owner_sid_string(self):  
        """Return the owner SID as a string in human readable format."""  
        if self.owner_sid is not None: 
            return win32security.ConvertSidToStringSid(self.owner_sid)  
        return None

    def sid_to_username_info(self, sid):  
        """
        Convert SID to username

        Args:
            SID (str): A Security Identifier.

        Returns:
            tuple: (
                Account Name (str),
                Domain Name (str),
                Account Type (str)
                )
        """  
        try:  
            account_name, domain_name, account_type = win32security.LookupAccountSid(None, sid)  
            return account_name, domain_name, account_type 
        except Exception as error:  
            raise RuntimeError(error)
        
    def access_info(self):
        """
        Convert SID to username

        Args:
            None
        Returns:
            tuple: (
                Account Name (str),
                Domain Name (str),
                Account Type (str)
                )
        """
        sid = self.get_owner_sid()
        return self.sid_to_username_info(sid)

import os  
import win32security  
import time  


class WindowsFileAccessInfo:  
    def __init__(self, file_path):  
        self.file_path = file_path  
        self.last_access_time = None  
        self.owner_sid = None  

    def get_file_stats(self):  
        """Get last access time and file owner SID."""  
        try:  
            stat_info = os.stat(self.file_path)  
            self.last_access_time = stat_info.st_atime  
            self.owner_sid = win32security.GetFileSecurity(  
                self.file_path,   
                win32security.OWNER_SECURITY_INFORMATION  
            ).GetSecurityDescriptorOwner()  
        except FileNotFoundError:  
            print("File not found.")  
            return False  
        except Exception as e:  
            print(f"An error occurred: {e}")  
            return False  
        return True  

    def get_last_access_time(self):  
        """Return last access time in a human-readable format."""  
        if self.last_access_time is not None:  
            return time.ctime(self.last_access_time)  
        return None  

    def get_owner_sid(self):  
        """Return the owner SID."""  
        if self.owner_sid is not None: 
            return self.owner_sid 
        return None
    
    def get_owner_sid_string(self):  
        """Return the owner SID as a string."""  
        if self.owner_sid is not None: 
            return win32security.ConvertSidToStringSid(self.owner_sid)  
        return None

    @staticmethod  
    def sid_to_username(sid):  
        """Convert SID to username."""  
        try:  
            account_name, domain_name, account_type = win32security.LookupAccountSid(None, sid)  
            return f"{domain_name}\\{account_name} (Account Type: {account_type})"  
        except Exception as e:  
            return f"Error: {e}"  
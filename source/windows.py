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
        if not self.last_access_time:  
            self.get_file_stats()
        return time.ctime(self.last_access_time)  

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

    def sid_to_username(self, sid):  
        """Convert SID to username."""  
        try:  
            account_name, domain_name, account_type = win32security.LookupAccountSid(None, sid)  
            return f"{domain_name}\\{account_name} (Account Type: {account_type})"  
        except Exception as e:  
            return f"Error: {e}"  

    def review(self):
        last_access_time = self.get_last_access_time()
        print(f"Last access time : {last_access_time}")
        sid_human_readable = self.get_owner_sid_string()
        print(f"Last access SID : {sid_human_readable}")
        sid = self.get_owner_sid()
        print(self.sid_to_username(sid=sid))

import os
import pwd
import grp
import time


class LinuxAccessWatch:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.get_file_stats()

    def get_file_stats(self):
        """Set last access time and file owner UID and GID."""
        try:
            stat_info = os.stat(self.file_path)
            self.last_access_time = stat_info.st_atime
            self.owner_uid = stat_info.st_uid
            self.owner_gid = stat_info.st_gid
        except FileNotFoundError:
            raise FileNotFoundError("File not found.")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

    def get_owner_uid(self):
        """Return the owner UID."""
        if self.owner_uid is not None:
            return self.owner_uid
        return None

    def get_owner_gid(self):
        """Return the owner GID."""
        if self.owner_gid is not None:
            return self.owner_gid
        return None

    def uid_to_username(self):
        """Convert UID to username."""
        try:
            uid = self.get_owner_uid()
            user_info = pwd.getpwuid(uid)
            return user_info.pw_name
        except KeyError as error:
            raise KeyError(f"UID {self.owner_uid} not found :{error}")

    def gid_to_groupname(self):
        """Convert GID to group name."""
        try:
            gid = self.get_owner_gid()
            group_info = grp.getgrgid(gid)
            return group_info.gr_name
        except KeyError as error:
            raise KeyError(f"GID {self.owner_gid} not found :{error}")

    def get_last_access_time(self):
        """Return last access time in a human-readable format."""
        if self.last_access_time is not None:
            return time.ctime(self.last_access_time)
        return None

    def get_username(self):
        return self.uid_to_username()
    
    def get_groupname(self):
        return self.gid_to_groupname()
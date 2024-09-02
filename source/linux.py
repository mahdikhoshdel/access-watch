import os
import pwd
import grp
import time


class LinuxAccessWatch:
    def __init__(self, file_path):
        self.file_path = file_path
        self.last_access_time = None
        self.owner_uid = None
        self.owner_gid = None

    def get_file_stats(self):
        """Get last access time and file owner UID and GID."""
        try:
            stat_info = os.stat(self.file_path)
            self.last_access_time = stat_info.st_atime
            self.owner_uid = stat_info.st_uid
            self.owner_gid = stat_info.st_gid
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

    def uid_to_username(self, uid):
        """Convert UID to username."""
        try:
            user_info = pwd.getpwuid(uid)
            return user_info.pw_name
        except KeyError:
            return f"UID {uid} not found"

    def gid_to_groupname(self, gid):
        """Convert GID to group name."""
        try:
            group_info = grp.getgrgid(gid)
            return group_info.gr_name
        except KeyError:
            return f"GID {gid} not found"
    
    def review(self):
        
        if self.get_file_stats():
            last_access_time = self.get_last_access_time()
            owner_uid = self.get_owner_uid()
            owner_gid = self.get_owner_gid()

            print(f"Last Access Time: {last_access_time}")

            if owner_uid is not None:
                username = self.uid_to_username(owner_uid)
                print(f"File Owner UID: {owner_uid} (Username: {username})")

            if owner_gid is not None:
                groupname = self.gid_to_groupname(owner_gid)
                print(f"File Owner GID: {owner_gid} (Group Name: {groupname})")

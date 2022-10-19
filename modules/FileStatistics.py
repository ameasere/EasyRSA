import platform
import os
import shutil
import psutil


class DriveStatistics:
    """
    Generate statistics for the parent drive.
    """

    def __init__(self):
        if platform.system() == "Darwin" or platform.system() == "Linux":
            self.parentDrive = '/'
        else:
            parentDrive = os.path.splitdrive(os.getcwd())[0]
            self.parentDrive = parentDrive
        stat = shutil.disk_usage(self.parentDrive)
        self.parentDriveSpace = (round((stat[1] / stat[0]) * 100))
        disk_info = []
        diskcounter = 0
        # The for loop iterates through the list of disk partitions returned by
        # psutil.disk_partitions(all=False).
        # The if statement checks is the parentDrive is in the first item in the list of disk
        # partitions.
        # If it is, the code breaks out of the for loop.
        # If it isn't, the code increments the diskcounter by 1 and continues the for loop.
        # The part variable is assigned to the disk partition that the parentDrive is in.
        for part in psutil.disk_partitions():
            if self.parentDrive in part[0]:
                part = psutil.disk_partitions()[diskcounter]
                break
            else:
                diskcounter += 1
        # If the partition is a cdrom drive, return 0.
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # Stop
                raise StopIteration("CDROM drive is not supported")
            else:
                pass
        usage = psutil.disk_usage(part.mountpoint)
        disk_info.append({
            'device': part.device,
            'total': usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': usage.percent,
            'fstype': part.fstype,
            'mountpoint': part.mountpoint
        })
        self.driveInformation = f"Device: {disk_info[0]['device']}\nTotal: {round(int(disk_info[0]['total']) / 1024 ** 3)} GB\nUsed: {round(int(disk_info[0]['used']) / 1024 ** 3)} GB\nFree: {round(int(disk_info[0]['free']) / 1024 ** 3)} GB\nPercent: {disk_info[0]['percent']}\nFS type: {disk_info[0]['fstype']}\nMount Point: {disk_info[0]['mountpoint']}"


class FileStatistics:
    """
    Generate statistics given a file's path
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.filesize = round(os.path.getsize(self.filepath) / 1024 ** 2)
        self.filetype = os.path.splitext(self.filepath)[1]
        self.filename = os.path.basename(self.filepath)
        self.checksum = self.getChecksum()
        self.permissions = self.getPermissions()
        self.owner = self.getOwner()

    def getChecksum(self):
        """
        Generate a checksum for the file.
        """
        import hashlib
        sha256_hash = hashlib.sha256()
        with open(self.filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def getPermissions(self):
        """
        Get the file's permissions. Returns octal permissions.
        """
        return oct(os.stat(self.filepath).st_mode)[-3:]

    def getOwner(self):
        """
        Get the file's owner.
        """
        return os.stat(self.filepath).st_uid

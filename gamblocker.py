import os
import pathlib


class GamBlocker():
    def __init__(self, os: str) -> None:
        self.os = os
        self.host_file = self.get_host_file()
        self.urls = self.get_urls()
        self.keywords 
        
    
    def get_host_file(self):
        """
        Get host file path
        """
        if self.os == "Windows":
            return pathlib.PureWindowsPath(__file__).root, "system32", "drivers", "etc", "hosts"
        elif self.os == "Linux":
            return "/etc/hosts"
        elif self.os == "Mac":
            return "/etc/hosts"
        else:
            return None
    
    def get_urls(self) -> list:
        """
        Get urls from file
        """
        with open((pathlib.Path(__file__).parent, "lists", "urls").__str__()) as f:
            return f.readlines()
    
    def get_keywords(self) -> list:
        """
        Get keywords from file
        """
        with open((pathlib.Path(__file__).parent, "lists", "keywords").__str__()) as f:
            return f.readlines()
    
    def update_host_file(self):
        """
        Update host file
        """
        with open(self.host_file, "r+") as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(url in line for url in self.urls):
                    f.write(line)
            f.truncate()

    def remove_all_blocks(self):
        """
        Remove all blocks
        """
        with open(self.host_file, "r+") as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if any(url in line for url in self.urls):
                    f.write(line)
            f.truncate()
    
    def remove_block(self, url):
        """
        Remove block
        """
        with open(self.host_file, "r+") as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if url in line:
                    f.write(line)
            f.truncate()
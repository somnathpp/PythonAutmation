#The configparser module in Python is used to handle configuration files in INI format. It allows reading, writing, and managing configurations with ease.
import configparser
import os

class ReadConfig:


    def __init__(self):
        self.config = configparser.RawConfigParser()
        config_path='.\\Configurations\\config.ini'
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")
        self.config.read(config_path)

    def getApplicationURL(self ):
        return self.config.get('common info','baseURL')
    def getUsername(self):
        return self.config.get('common info','username')
    def getPassword(self):
        return self.config.get('common info','password')


import configparser
import os

config = configparser.RawConfigParser()
# config.read(os.path.realpath(os.curdir) + '..\\config\\config.ini')

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(base_dir, "config", "config.ini")
config.read(config_path)

class ReadConfig():

    @staticmethod
    def get_application_URl():
        baseURL = (config.get(section='commonInfo' , option='baseURL'))
        return baseURL

    @staticmethod
    def get_email():
        email = (config.get(section='commonInfo' , option='email'))
        return email
        
    @staticmethod
    def get_uname():
        username = (config.get(section='commonInfo' , option='user_name'))
        return username
    
    @staticmethod
    def get_password():
        password = (config.get(section='commonInfo' , option='user_name'))
        return password
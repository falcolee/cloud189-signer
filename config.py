import os
import platform
import sys

TEST_MODE = False
DEFAULT_THEME = 'DarkGrey2'
default_font = 'Helvetica 12'
sett_folder = None
operating_system = platform.system()
settings_keys = ['username', 'password', 'DEFAULT_THEME']
username = ''
password = ''
# folders
if hasattr(sys, 'frozen'):  # like if application froen by cx_freeze
    current_directory = os.path.dirname(sys.executable)
else:
    path = os.path.realpath(os.path.abspath(__file__))
    current_directory = os.path.dirname(path)
sys.path.insert(0, os.path.dirname(current_directory))
sys.path.insert(0, current_directory)

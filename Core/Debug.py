import os
import inspect
from datetime import datetime

COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_RED = '\033[91m'
COLOR_RESET = '\033[0m'


class Debug:
    @staticmethod
    def log(message):
        caller_class_name = f"{os.path.basename(inspect.currentframe().f_back.f_code.co_filename)} -> {inspect.currentframe().f_back.f_code.co_name}()"
        print(f"{COLOR_GREEN}[{Debug.get_time()}] [{caller_class_name}] {message}{COLOR_RESET}")

    @staticmethod
    def warning(message):
        caller_class_name = f"{os.path.basename(inspect.currentframe().f_back.f_code.co_filename)} -> {inspect.currentframe().f_back.f_code.co_name}()"
        print(f"{COLOR_YELLOW}[{Debug.get_time()}] [{caller_class_name}] {message}{COLOR_RESET}")

    @staticmethod
    def error(message):
        caller_class_name = f"{os.path.basename(inspect.currentframe().f_back.f_code.co_filename)} -> {inspect.currentframe().f_back.f_code.co_name}()"
        print(f"{COLOR_RED}[{Debug.get_time()}] [{caller_class_name}] {message}{COLOR_RESET}")

    @staticmethod
    def get_time():
        return datetime.now().strftime("%H:%M:%S")

from datetime import datetime

COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_RED = '\033[91m'
COLOR_RESET = '\033[0m'


class Debug:
    @staticmethod
    def log(message):
        print(f"{COLOR_GREEN}[{Debug.get_time()}] {message}{COLOR_RESET}")

    @staticmethod
    def warning(message):
        print(f"{COLOR_YELLOW}[{Debug.get_time()}] {message}{COLOR_RESET}")

    @staticmethod
    def error(message):
        print(f"{COLOR_RED}[{Debug.get_time()}] {message}{COLOR_RESET}")

    @staticmethod
    def get_time():
        return datetime.now().strftime("%H:%M:%S")

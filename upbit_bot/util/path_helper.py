import os

class PathHelper():
    @staticmethod
    def get_user_data_path():
        return os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + 'bot' + os.sep + 'data' + os.sep + 'user.json')
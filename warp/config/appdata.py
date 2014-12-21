import appdirs
import os
import warp.os
import shutil

import warp.logging
log = warp.logging.get_logger(__name__)

class AppData(object):

    """docstring for AppData"""

    def __init__(self, app_name, script_path, develop=False):
        super(AppData, self).__init__()
        self.app_name = app_name
        self.script_path = script_path
        self.script_root_path = os.path.dirname(
            os.path.dirname(os.path.abspath(self.script_path)))
        self.script_config_path = os.path.join(self.script_root_path, "config")
        self.develop = develop

    @property
    def default_config_dir(self):
        return appdirs.user_config_dir(self.app_name)

    @property
    def default_data_dir(self):
        return appdirs.user_data_dir(self.app_name)

    @property
    def data_paths(self):
        paths = [self.default_data_dir,
                 os.path.join(self.script_root_path, "data")]
        return paths

    @property
    def config_paths(self):
        paths = [self.default_config_dir,
                 os.path.join(self.script_root_path, "config")
                 ]
        return paths

    def __get_file_path(self, paths, name):
        for path in paths:
            full_path = os.path.join(path, name)
            if os.path.isfile(full_path):
                break
        else:
            full_path = os.path.join(paths[0], name)

        if not self.develop:
            default_file_path = os.path.join(paths[0], name)
            if not full_path == default_file_path and self.script_root_path in full_path:
                warp.os.makedirs(paths[0], exist_ok=True)
                shutil.copyfile(full_path, default_file_path)
                return default_file_path

        return full_path

    def get_config_file_path(self, name):
        return self.__get_file_path(self.config_paths, name)

    def get_data_file_path(self, name):
        return self.__get_file_path(self.data_paths, name)



def main():

    appdata = AppData("tarsync", os.path.realpath(__name__))

    # print appdata.app_name
    # print appdata.script_path
    # print appdata.default_config_dir
    # print appdata.default_data_dir
    # print appdata.script_root_path
    # print appdata.script_config_path

    # print appdata.get_config_file_path("1tarsync.json")
    print appdata.get_data_file_path("1tarsync.json")
    # print appdata.get_data_file_path("tarsync.json")
if __name__ == '__main__':
    main()

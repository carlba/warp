import appdirs
import os
import json
import errno
import shutil


import warp.os
import warp.logging
log = warp.logging.get_logger(__name__)


class ConfigHandler(object):

    '''  Reads a config-file from a provided path'''

    def __init__(self, path):
        self.path = path
        self.info = {"system": type(self).__name__}
        self._config = {}

    def __store_dict_to_file(self, filename, thedict):
        with open(filename, "w+") as jsonfile:
            jsonfile.write(json.dumps(thedict, indent=4))

    def __read_dict_from_file(self, filename):
        with open(filename, "r+") as jsonfile:
            return json.loads(jsonfile.read())

    def load(self):
        self._config = self.__read_dict_from_file(self.path)

    @property
    def config(self):
        return self._config


if __name__ == '__main__':
    config = ConfigHandler(
        script_path=os.path.abspath(__file__), app_name="tarsync")
    config.load()
    print config.config

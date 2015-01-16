import shutil
import sys
import os
import stat
import errno
import subprocess
import datetime

def safe_remove_folder(folder):
    if sys.platform.startswith('win'):
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder, topdown=False):
                for name in files:
                    filename = os.path.join(root, name)
                    os.chmod(filename, stat.S_IWRITE)
                    os.remove(filename)
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(folder)
    else:
        shutil.rmtree(folder)


def makedirs(path, exist_ok=False):
    if exist_ok:
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise
    else:
        os.makedirs(path)


def locate(pattern, **kwargs):

    args = ["locate"]
    if "regex" in kwargs:
        args.append("--regex")

    args.append(pattern)

    return subprocess.check_output(args).split()


class Path(object):
    """docstring for Path"""
    def __init__(self, path):
        super(Path, self).__init__()
        self.path = path
        

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

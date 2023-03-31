import logging
import os


def find_directory():
    directory = str(os.getcwd())+"\\Log"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def log_files(name):
    directory = find_directory()
    logging.basicConfig(filename='%s\\%s.log' % (directory, name),
                            filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
    result_logger = logging.getLogger(name)
    return result_logger



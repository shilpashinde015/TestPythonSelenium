import inspect
import os
from datetime import datetime
import logging.config


def Logs_util(log_level=logging.INFO):
    log_filename = None

    cur_path = os.path.abspath(os.path.dirname(__file__))
    dir_log = os.path.join(cur_path, r"/home/shilpa/Git/TestPythonSelenium/ScriptLogs/")

    if not os.path.exists(dir_log):
        os.mkdir(dir_log)

    date_dir = os.path.join(dir_log, str(datetime.strftime(datetime.now(), '%d%m%Y')))

    if not os.path.exists(date_dir):
        os.mkdir(date_dir)

    current_time = datetime.strftime(datetime.now(), '%d%m%Y-%H%M%S')
    # log_filename = os.path.join(date_dir, 'test.log')

    if log_filename is None:
        log_file = "test" + current_time + ".log"
        log_filename = os.path.join(date_dir, log_file)

    call_name = inspect.stack()[1][1] + " - \tLN:" + str(inspect.stack()[1][2])
    call_name = str(call_name)
    #
    # logging.basicConfig(filename=log_filename, format='%(asctime)s - %(levelname)s - %(message)s')
    # # logger = logging.getLogger(caller_name)
    # logger = logging.getLogger()
    #
    # # Set logging level for logger
    # logger.setLevel(log_level)

    fhandler = logging.FileHandler(filename=log_filename, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhandler.setFormatter(formatter)
    logger = logging.getLogger(call_name)
    logger.addHandler(fhandler)
    logger.setLevel(logging.DEBUG)
    return logger

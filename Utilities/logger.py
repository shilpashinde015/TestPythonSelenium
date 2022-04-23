
import logging


class LogGen:
    # @staticmethod
    # def loggen():
    #     logging.basicConfig(filename="test.log",
    #                         format='%(asctime)s %(message)s',
    #                         filemode='w')
    #
    #     # Creating an object
    #     logger = logging.getLogger()
    #     return logger
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='mylog.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.DEBUG)
        return logger
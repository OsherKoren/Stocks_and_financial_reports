import logging

# Logger configuration:
class Mylogger:
    def __init__(self, loggerName):
        self.loggerName = loggerName

    def log(self):
        logger = logging.getLogger(self.loggerName)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")

        # Create handlers and set levels
        file_handler = logging.FileHandler(self.loggerName + '.log',  mode='w')
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger

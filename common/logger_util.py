import logging

class LoggerUtil:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._logger_setup()
        return cls._instance

    def _logger_setup(self):
        self.logger = logging.getLogger('mylogger')
        self.logger.setLevel(logging.INFO)

        date_format = "%Y-%m-%d %H:%M:%S"
        fh = logging.FileHandler('./PytestLog/log.txt', mode='a', encoding='utf-8')
        sh = logging.StreamHandler()

        fmt = logging.Formatter('%(asctime)s - %(levelname)s - <%(filename)s:%(lineno)s> - %(message)s', datefmt=date_format)
        fh.setFormatter(fmt=fmt)
        sh.setFormatter(fmt=fmt)

        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def get_logger(self):
        return self.logger

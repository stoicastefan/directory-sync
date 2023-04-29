import logging


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s [%(levelname)s] %(message)s',
                handlers=[
                    logging.FileHandler('log_file.log'),
                    logging.StreamHandler()
                ]
            )
        return cls._instance

    def create_info_log(self, message):
        logging.log(logging.INFO, message)

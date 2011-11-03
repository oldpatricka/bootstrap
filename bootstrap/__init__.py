
from config import Config

DEFAULT_CONFIG_FILES = ['config/service.yml', 'config/service.local.yml']

class Service(object):
    """Base class for services. Meant to be subclassed

    """

    def __init__(self, config_files=DEFAULT_CONFIG_FILES):

        self.CFG = Config(config_files).data


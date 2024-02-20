import logging # Documentation: https://docs.python.org/3/library/logging.html#module-logging
import logging.config # Documentation: https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig
from my_internet_resource import *
from my_preprocessor import *

# Logging configuration file
# Loggers: root, my_internet_resource, my_preprocessor
# Handlers: File handler, stream handler
logging.config.fileConfig("./my_logging.ini")
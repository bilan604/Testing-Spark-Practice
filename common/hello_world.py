import logging
from logging.config import fileConfig


fileConfig('logging.ini')
logger = logging.getLogger(__name__)


def main():
    logger.info("Hello world")
    

if __name__ == "__main__":
    main()
from configparser import ConfigParser
from docker import client

class containerUtil():

    cfg = ConfigParser()

    def __init__(self, cli):
        # self.cli =
        self.cli = cli


    # def print_status(self):
        # self.cli.
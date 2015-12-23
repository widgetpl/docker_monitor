import configparser
import sys

class Config():

    config = configparser.ConfigParser()

    def __init__(self, cfg_file="../resources/config.ini"):
        self.config.read(cfg_file)


    def print_config_sections(self):
        for i in self.config.sections():
            print("[{}]".format(i))

    def print_whole_config(self):
        for i in self.config.sections():
            print("[ {} ]".format(i))
            for j in self.config[i]:
                print("\t{} = {}".format(j, self.config[i][j]))
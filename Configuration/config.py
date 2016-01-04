from configparser import ConfigParser
import sys

class Config():

    def __init__(self, cfg_file='../resources/config.ini'):
        # configparser.ConfigParser.__init__(self)
        self.config = ConfigParser()
        self.config.read(cfg_file)

    def print_config_sections(self):
        for i in self.config.sections():
            print("[{}]".format(i))

    def print_whole_config(self):
        for i in self.config.sections():
            print("[ {} ]".format(i))
            for j in self.config[i]:
                print("\t{} = {}".format(j, self.config[i][j]))
                # print("\ttype: {}".format(type(self.config.sections()[i][j])))

    def get_section_by_index(self, index):
        return self.config.sections().__getitem__(index)

    def get_config(self):
        return self.config


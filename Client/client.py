from docker import Client
from Configuration import config
from Utils import containersUtil
from configparser import ConfigParser
import ast
import json
import pprint
from Utils import bcolors

class Cli(object):

    def __init__(self, cfg):
        self.cfg = cfg
        self.cli = Client()


    def check_connectivity(self):
        print("Checking connectivity with hosts from config file:")
        for h in self.cfg.sections():
            if Client(base_url="http://{}:{}".format(self.cfg[h]["host"], self.cfg[h]["port"])):
                Client(base_url="http://{}:{}".format(self.cfg[h]["host"], self.cfg[h]["port"]))
                print("{} : {}{}{}".format(h,bcolors.Bcolors.OKGREEN,"OK",bcolors.Bcolors.ENDC))
            else:
                print("{} : {}".format(h,"NOT OK"))
            # print("{} : {}".format(h,Client(base_url="http://{}:{}".format(self.cfg[h]["host"], self.cfg[h]["port"]))))








# host = "172.16.224.64"
# host = '127.0.0.1'
# port = 5555
# cli = Client(base_url='unix://var/run/docker.sock')
# cli = Client(base_url="http://{}:{}".format(host, port))
#status = cli.__getstate__()
#for i in status:
#    print(type(i))
#    print('{}: {}'.format(i, status[i]))
#print(len(cli.containers()))
#dict = cli.containers()[0]
# print(type(dict))

# for dict in cli.containers():
#     for i in ("Names","Status","Image"):
#         print("{} : {}".format(i, dict[i]))
#         #print("type: {}".format(type(i)))
#     print("\n\n\n")



cfg = ConfigParser()
# cfg = config.Config()
cfg.read('../resources/config.ini')
# cu = containersUtil.containerUtil(cfg)


# for sect in cfg.sections():
#     print(sect)
#     temp = cfg[sect]
#     print("Host: {}".format(sect))
#     print("\thost: {}".format(temp["host"]))
#     print("\tport: {}".format(temp["port"]))

for sect in cfg.sections():
    temp = cfg[sect]
    print(cfg[sect]["host"])
    print(cfg[sect]["port"])
    cli = Client(base_url="http://{}:{}".format(temp["host"], temp["port"]))

    print("\n" + sect)
    for dict in cli.containers():
        print("\n")
        print("\t" + str(dict['Names'][0]))
        print("\t" * 2 + "[Status]: " + dict['Status'])
        print("\t" * 2 + "[Image]: " + dict['Image'])
        if 'Ports' in dict:
            for p in dict['Ports']:
                port = '\t'
                if 'PrivatePort' in p:
                    # print("\tPrivate port: " + str(p['PrivatePort']))
                    port = port + '[Private port]: ' + str(p['PrivatePort'])
                if 'PublicPort' in p:
                    # print("\tPublic port: " + str(p['PublicPort']))
                    port = port + ' [Public port]: ' + str(p['PublicPort'])
                if 'IP' in p:
                    port = port + ' [IP]: ' + str(p['IP'])
                if 'Type' in p:
                    port = port + ' [Type]: ' + str(p['Type'])
                print("\t" + port)
            # print(dict)

        # print(cli.inspect_container(dict['Id']))
        temp = cli.inspect_container(dict['Id'])
        print(temp['State']['StartedAt'])
        print(temp['Created'])
        # print(type(temp))
        # data = json.loads(json.dumps(str(cli.inspect_container(dict['Id']))))
        # data = json.dumps(str(temp))
        # print(data["HostsPath"])
        # print(data)

        # for inspect_dict in cli.inspect_container(dict['Id']):
        #     print(type(inspect_dict))





# cfg.print_config_sections()
# cfg.print_whole_config()
#
# print(cfg.get_section_by_index(0))
# print(len(cfg.get_section_by_index(0)))
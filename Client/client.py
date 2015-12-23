from docker import Client
from Configuration import config

#host = "172.16.224.64"
host = 'localhost'
port = 5555

#cli = Client(base_url='unix://var/run/docker.sock')
cli = Client(base_url="http://{}:{}".format(host, port))

#status = cli.__getstate__()
#for i in status:
#    print(type(i))
#    print('{}: {}'.format(i, status[i]))
#print(len(cli.containers()))
#dict = cli.containers()[0]

print(type(dict))

for dict in cli.containers():
    for i in ("Names","Status","Image"):
        print("{} : {}".format(i, dict[i]))
        #print("type: {}".format(type(i)))
    print("\n\n\n")


cfg = config.Config()
cfg.print_config_sections()
cfg.print_whole_config()
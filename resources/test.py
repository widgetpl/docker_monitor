from docker import Client
from Utils import bcolors


cli = Client(base_url="http://172.16.224.64:5555")


# print("Containers:")
# print(cli.containers())
# print(type(cli.containers()))
# print("Number of running containers: " + str(len(cli.containers())))


# print(cli.containers()[0])

def dictionary_loop(d):
    for key, value in d.items():
        if isinstance(value, list):
            list_loop(value)
        elif isinstance(value, dict):
            print("### " + str(key) + " ###")
            dictionary_loop(value)
        else:
            print("{} : {}".format(key, value))


def list_loop(l):
    for i in l:
        if isinstance(i, list):
            list_loop(i)
        elif isinstance(i, dict):
            dictionary_loop(i)
        else:
            print(str(i))

def display_container_info(cont):
    print(bcolors.Bcolors.BOLD+"Container ID: "+bcolors.Bcolors.ENDC + cont["Id"])
    print(bcolors.Bcolors.BOLD+"Command run by container: "+bcolors.Bcolors.ENDC + cont["Command"])
    print(bcolors.Bcolors.BOLD+"Container status: "+bcolors.Bcolors.ENDC + cont["Status"])
    print(bcolors.Bcolors.BOLD+"Container image: "+bcolors.Bcolors.ENDC + cont["Image"])
    print(bcolors.Bcolors.BOLD+"Container name: "+bcolors.Bcolors.ENDC + cont["Names"][0])
    print(bcolors.Bcolors.BOLD+"Number of ports: "+bcolors.Bcolors.ENDC + str(len(cont["Ports"])))
    for i in cont["Ports"]:
        for key, value in i.items():
            # print("{}:".format(i["PrivatePort"]))
            # if "PublicPort" in i:
            #     print("\tPublic port: " + )
            print("\t{} : {}".format(key, value))
        print("")

def display_container_inspect(cont):
    print("Container name: {}".format(cont["Name"]))
    print()

# for i in cli.containers():
#     print()
#     print(i)
#     print(type(i))

# display_container_info(cli.containers()[0])
#

print(cli.inspect_container(cli.containers()[0]))

cli.

# if isinstance(cli.containers(), list):
#     list_loop(cli.containers())
# elif isinstance(cli.containers(), dict):
#     dictionary_loop(cli.containers())
# else:
#     print("It's not instance of list or dict. It is instance of: " + str(type(cli.containers())))


# print(cli.containers()[0])





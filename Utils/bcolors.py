class Bcolors:
    HEADER = '\033[1;95m'
    OKBLUE = '\033[1;94m'
    OKGREEN = '\033[1;92m'
    WARNING = '\033[1;93m'
    FAIL = '\033[1;91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
#
# print bcolors.WARNING + "Warning: No active frommets remain. Continue?"
#       + bcolors.ENDC
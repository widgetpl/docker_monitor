__appname__ = 'docker-monitor'
__version__ = '0.1.0'
__author__ = 'Mike Dziedziela <michal.dziedziela@gmail.com'

# import docker-monitor libs
from monitor.core import monitor_globals


def main():
    """ Main entry point for docker-monitor

    """

    global core, standalone

    print(monitor_globals.appname)
    print(monitor_globals.version)

    from monitor.core.monitor_standalone import
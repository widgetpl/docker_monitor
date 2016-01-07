__appname__ = 'docker-monitor'
__version__ = '0.1.0'
__author__ = 'Mike Dziedziela <michal.dziedziela@gmail.com'

# Import system libs
import sys

# import docker-monitor libs
from monitor.core import monitor_globals


try:
    from docker import __version__ as __docker_py_version
except ImportError:
    print('docker-py library not found. Docker-monitor cannot start.')
    sys.exit(1)

def main():
    """ Main entry point for docker-monitor

    """

    global core, standalone

    core =

    print(monitor_globals.appname)
    print(monitor_globals.version)

    from monitor.core.monitor_standalone import MonitorStandalone

    standalone = MonitorStandalone(config=)
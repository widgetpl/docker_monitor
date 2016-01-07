# Import system libs
import sys
try:
    from configparser import ConfigParser
    from configparser import NoOptionError
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser
    from ConfigParser import NoOptionError

# Import monitor libs
from monitor.core.monitor_globals import (
    appname,
)


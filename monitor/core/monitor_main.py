# Import system libs
import argparse

# Imports
from monitor.core.monitor_globals import appname, version, dockerpy_version

class MonitorMain(object):

    """ Main class to manage Monitor instance
    """

    # Default stats' refresh time is 3 seconds
    refresh_time = 3

    # To be done much later ( server, client )
    # Server TCP port number ( default is 61209 )
    # server_port = 61209
    # Web Server TCP port number ( default is 61208 )
    # web_server_port = 61208
    # Default username/password for client/server mode
    # username = "monitor"
    # password = ""


    example_of_use = "\
Examples of use:\n\
\n\
Monitor local machine (standalone mode):\n\
  $ glances\n\
\n\
Monitor local machine with the Web interface (Web UI):\n\
  $ glances -w\n\
  Glances web server started on http://0.0.0.0:61208/\n\
\n\
Monitor local machine and export stats to a CSV file (standalone mode):\n\
  $ glances --export-csv\n\
\n\
Monitor local machine and export stats to a InfluxDB server with 5s refresh time (standalone mode):\n\
  $ glances -t 5 --export-influxdb\n\
\n\
Start a Glances server (server mode):\n\
  $ glances -s\n\
\n\
Connect Glances to a Glances server (client mode):\n\
  $ glances -c <ip_server>\n\
\n\
Connect Glances to a Glances server and export stats to a StatsD server (client mode):\n\
  $ glances -c <ip_server> --export-statsd\n\
\n\
Start the client browser (browser mode):\n\
  $ glances --browser\n\
    "

    def __init__(self):
        """ Manage the command line arguments """

        self.args = self.parse_args()


    def init_args(self):
        _version = "Monitor v" + version + " with docker-py v" + dockerpy_version

        parser = argparse.ArgumentParser(
            prog=appname,
            conflict_handler='resolve',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=self.example_of_use
        )

        # TODO
        # add arguments
        parser.add_argument()

        return parser


    def parse_args(self):
        return 0
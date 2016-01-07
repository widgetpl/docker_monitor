from Client import client
from Configuration import config


cfg = config.Config(cfg_file="resources/config.ini")
cli = client.Cli(cfg=cfg.get_config())

cli.check_connectivity()


# cfg.print_config_sections()
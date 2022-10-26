from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "_waqi"

CONF_KEYWORD = "keyword"
CONF_STATION = "station"
CONF_UPDATE_INTERVAL = "update_interval"

DEFAULT_UPDATE_INTERVAL = 900

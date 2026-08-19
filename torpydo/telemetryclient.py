import logging
import tomllib

from azure.monitor.opentelemetry import configure_azure_monitor

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

connection_string = config["telemetry"]["connection_string"]

configure_azure_monitor(
    logger_name=__name__,
    connection_string=connection_string),
logger = logging.getLogger(__name__)

class TelemetryClient(object):
    def init():
        logger.setLevel(logging.INFO)

    def trackEvent(eventName: str, properties: object):
        logger.info(eventName, extra=properties)

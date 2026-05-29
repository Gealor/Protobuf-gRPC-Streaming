import logging

LOG_DEFAULT_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)
level: int = logging.INFO
datefmt: str = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    format=LOG_DEFAULT_FORMAT,
    datefmt=datefmt,
    level=level,
)

log = logging.getLogger(__name__)
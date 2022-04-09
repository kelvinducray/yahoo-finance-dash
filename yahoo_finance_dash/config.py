from functools import lru_cache
from os import getenv

from pydantic import BaseSettings


class DevSettings(BaseSettings):
    ENVIRONMENT_NAME = "Development"

    YAHOO_FINANCE_API_KEY: str

    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "coloredlogs.ColoredFormatter",
                "fmt": "%(asctime)s %(levelname)s %(name)s — %(message)s",
            }
        },
        "handlers": {
            "default": {
                "()": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["default"]},
    }

    class Config:
        env_file = ".env"


class ProdSettings(BaseSettings):
    ENVIRONMENT_NAME = "Production"


@lru_cache
def get_settings() -> DevSettings | ProdSettings:
    if getenv("DEPLOYED_ENVIRONMENT") == "PROD":
        return ProdSettings()
    else:
        return DevSettings()

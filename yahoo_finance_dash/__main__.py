from logging.config import dictConfig

from .app import app
from .config import get_settings

settings = get_settings()

if __name__ == "__main__":
    # dictConfig(settings.LOGGING_CONFIG)
    if settings.ENVIRONMENT_NAME == "Production":
        pass
    else:
        app.run_server(debug=True)

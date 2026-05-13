'''
All things logging
'''

import getpass
import logging.config
import shutil
import sys
from pathlib import Path
import yaml

from . import __version__

_logging_configured = False

CARAGOLS_CONFIG_DIR = Path.home() / '.config' / 'caragols'
LOGGING_CONFIG_TEMPLATE_PATH = Path(__file__).parent / 'logging-config.yaml'
LOGGING_CONFIG_DEFAULT_PATH = CARAGOLS_CONFIG_DIR / 'logging-config.yaml'


def initialize_logging_config() -> Path:
    '''Copy the template config to ~/.config/caragols/ if not already present.'''
    if not LOGGING_CONFIG_DEFAULT_PATH.exists():
        LOGGING_CONFIG_DEFAULT_PATH.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(LOGGING_CONFIG_TEMPLATE_PATH, LOGGING_CONFIG_DEFAULT_PATH)
    return LOGGING_CONFIG_DEFAULT_PATH


def config_logging_for_app(app_name: str = 'app'):
    """Configure logging for a CLI app, writing logs to ~/.config/caragols/<app_name>/."""
    global _logging_configured

    if _logging_configured:
        return

    yaml_config = yaml.safe_load(initialize_logging_config().read_text())

    log_dir = CARAGOLS_CONFIG_DIR / app_name
    if yaml_config.get('use_user_subdir'):
        log_dir /= getpass.getuser()
    log_dir.mkdir(parents=True, exist_ok=True)

    console_log_level = yaml_config.get('console_log_level', 'INFO')

    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "caragols_basicFormatter": {
                "format": "[%(asctime)s %(levelname)s %(name)s] - %(message)s",
                "datefmt": "%H:%M:%S",
            },
            "caragols_verboseFormatter": {
                "format": "[%(asctime)s %(levelname)s %(process)d %(filename)s:%(funcName)s:%(lineno)d] - %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S%z",
            },
            "caragols_jsonFormatter": {
                "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "datefmt": "%Y-%m-%dT%H:%M:%S%z",
                "format": "%(asctime)s.%(msecs)03d %(levelname)s %(name)s %(filename)s %(module)s %(process)d %(processName)s %(thread)d %(funcName)s %(lineno)d %(message)s",
            },
        },
        "handlers": {
            "caragols_consoleHandler": {
                "level": console_log_level,
                "class": "logging.StreamHandler",
                "formatter": "caragols_basicFormatter",
                "stream": sys.stdout,
            },
            "caragols_plaintextFileHandler": {
                "level": "DEBUG",
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "caragols_verboseFormatter",
                "filename": str(log_dir / 'log.txt'),
                "maxBytes": 2000000,
                "backupCount": 100,
            },
            "caragols_jsonFileHandler": {
                "level": "DEBUG",
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "caragols_jsonFormatter",
                "filename": str(log_dir / 'log.jsonl'),
                "maxBytes": 2000000,
                "backupCount": 100,
            },
        },
        "loggers": {
            app_name: {
                "level": "DEBUG",
                "handlers": ["caragols_consoleHandler", "caragols_plaintextFileHandler", "caragols_jsonFileHandler"],
                "propagate": False,
            },
        },
    }

    logging.config.dictConfig(config=log_config)
    logger = logging.getLogger(app_name)
    logger.debug('Startup: %s', {'cwd': str(Path.cwd()), 'user': getpass.getuser(), 'argv': sys.argv, 'version': __version__})
    _logging_configured = True

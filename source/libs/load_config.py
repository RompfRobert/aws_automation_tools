import json
import logging

CONFIG_FILE = '~/.aws_automation_tools/config.json'

def load_config():
    """
    Load configuration from a JSON file.
    """
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file {CONFIG_FILE} not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Configuration file {CONFIG_FILE} contains invalid JSON.")

    if 'account_ids' not in config or 'region' not in config:
        raise KeyError("Configuration must contain 'accounts' and 'region' keys.")

    logging.debug(config)
    return config
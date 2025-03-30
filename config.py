from dotenv import load_dotenv
import os


def load_env(config_file: str = None):
    # Load environment variables from .env file
    load_dotenv()
    if config_file:
        with open(config_file, "r") as f:
            for line in f:
                key, _, value = line.strip().partition("=")
                os.environ[key] = value

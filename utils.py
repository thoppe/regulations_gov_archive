import os
import requests
from requests.adapters import HTTPAdapter


def get_session():
    session = requests.Session()
    session.mount("https", HTTPAdapter(max_retries=4))
    return session


def get_API_KEY():
    env_key = "REGULATIONS_GOV_API_KEY"

    try:
        api_key = os.environ[env_key]
    except KeyError:
        raise KeyError(f"Env variable: {env_key} not found")

    headers = {"X-Api-Key": api_key}

    return headers

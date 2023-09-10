import os
import requests
from requests.adapters import HTTPAdapter
import time


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


def sleep_if_needed(r, buffer_seconds=5):
    """
    Input: requests response

    regulations.gov gives 'Retry-After' in the header for how long to wait.
    Use this to sleep for that amount of time plus a buffer if needed.
    """
    sleep_time = int(r.headers["Retry-After"]) + buffer_seconds
    print(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time + 4)

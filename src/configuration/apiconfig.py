import os
from dotenv import load_dotenv

load_dotenv()


class ApiConfig:

    __DEFAULT_URL = "https://api.unsplash.com/photos/random"
    __DEFAULT_CILENT = "MC663BMbexyv09hkiF8ZhcJwOQcfVtxJge26wtJtTmw"
    __DEFAULT_COUNT = "10"
    __DEFAULT_QUERY = "dog"
    __DEFAULT_ORIENTATION = "landscape"

    url = os.getenv("URL", default=__DEFAULT_URL)
    client_id = os.getenv("CLIENT_ID", default=__DEFAULT_CILENT)
    count = os.getenv("COUNT", default=__DEFAULT_COUNT)
    query = os.getenv("QUERY", default=__DEFAULT_QUERY)
    orientation = os.getenv("ORIENTATION", default=__DEFAULT_ORIENTATION)

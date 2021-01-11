import os
from dotenv import load_dotenv

load_dotenv()


class Schedule:
    # At every minute.
    __DEFAULT_MINUTE = "*"
    __DEFAULT_HOUR = "*"
    __DEFAULT_DAY_OF_MONTH = "*"
    __DEFAULT_MONTH = "*"
    __DEFAULT_DAY_OF_WEEK = "*"

    minute = os.getenv("MINUTE", __DEFAULT_MINUTE)
    hour = os.getenv("HOUR", __DEFAULT_HOUR)
    day_of_month = os.getenv("DAY_OF_MONTH", __DEFAULT_DAY_OF_MONTH)
    month = os.getenv("MONTH", __DEFAULT_MONTH)
    day_of_week = os.getenv("DAY_OF_WEEK", __DEFAULT_DAY_OF_WEEK)

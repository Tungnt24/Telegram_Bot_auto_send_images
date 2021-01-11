import functools
from celery import Task
import logging

from telebot.types import WebhookInfo
from src.configuration.teleconfig import BotConfig

from src.libs.client.telegram import Telegram

logging.basicConfig(
    format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)
logger = logging.getLogger(__name__)


def send_message(message: str):
    tele = Telegram()
    tele.send_message(BotConfig.group_id, message=message)


def before_task_run(_func, _args=None, _kwargs=None):
    if not _args:
        _args = []
    if not _kwargs:
        _kwargs = dict()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            _func(**_kwargs)
            func(*args, **kwargs)

        return wrapper

    return decorator


def error(kwargs):
    func_name = kwargs.get("func_name")
    exc = kwargs.get("exc")
    tele = Telegram()
    tele.send_message(
        BotConfig.group_id,
        message=f"FUNC: {func_name} | ERROR: {exc}",
    )
    raise exc


def task_error_handle(_func):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            try:
                return func(*args)
            except Exception as exc:
                _func({"func_name": func.__name__, "exc": exc})

        return wrapper

    return decorator


def retry(times: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(task: Task, *args):
            task.max_retries = times
            try:
                result = func(task, *args)
            except Exception as exc:
                raise task.retry(exc=exc, countdown=5)
            else:
                return result

        return wrapper

    return decorator

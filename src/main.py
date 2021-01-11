from celery import Celery, chain
from multiprocessing import Process
from functools import partial
from src.app.schedule import schedule_task

app = Celery("tasks", include=["src.logic.unsplash_image"])

app.config_from_object("src.configuration.celeryconfig")


def worker():
    w = app.Worker(
        include=["src.app.schedule"],
        loglevel="INFO",
    )
    w.start()


def beat():
    app.conf.beat_schedule = schedule_task
    app.conf.timezone = "UTC"
    b = partial(app.Beat, loglevel="debug")
    b().run()


if __name__ == "__main__":
    w = Process(target=worker)
    b = Process(target=beat)
    w.start()
    b.start()

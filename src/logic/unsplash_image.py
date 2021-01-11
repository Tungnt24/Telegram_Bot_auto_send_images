from typing import List
from celery import Task
import os
import glob
import urllib
import logging
from src.main import app, chain
from src.libs import decorators

from src.configuration.teleconfig import BotConfig
from src.libs.client.unsplash import Unsplash
from src.libs.client.telegram import Telegram
from src.configuration.apiconfig import ApiConfig

logging.basicConfig(
    format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)
logger = logging.getLogger(__name__)


@app.task(bind=True)
@decorators.retry(10)
@decorators.task_error_handle(decorators.error)
def get_images(self: Task) -> List:
    unsplash = Unsplash()
    response = unsplash.get_images(
        ApiConfig.client_id,
        ApiConfig.count,
        ApiConfig.query,
        ApiConfig.orientation,
        ApiConfig.url,
    )
    images = [image["urls"]["regular"] for image in response.json()]
    logger.info("GET IMAGES DONE!!")
    return images


@app.task
@decorators.task_error_handle(decorators.error)
def save_image(images: List[str]):
    images_path = f"{os.getcwd()}/src/images"
    if not os.path.exists(images_path):
        os.mkdir(images_path)

    for numb, url in enumerate(images, start=1):
        urllib.request.urlretrieve(url, f"{images_path}/{numb}.jpeg")
    logger.info("IMAGES HAVE BEEN DOWNLOADED")
    images_path = f"{images_path}/*.jpeg"
    return images_path


@app.task
@decorators.task_error_handle(decorators.error)
def get_image_files(path: str) -> List:
    image_files = [image for image in glob.glob(path)]
    return image_files


@app.task
@decorators.task_error_handle(decorators.error)
@decorators.before_task_run(
    decorators.send_message, _kwargs={"message": "SEND_IMAGES"}
)
def send_image(images_files: List[str]):
    tele = Telegram()
    for image in images_files:
        tele.send_image(BotConfig.group_id, open(image, "rb"))
    logger.info("SEND IMAGE DONE!")


@app.task
def execute():
    chain(
        get_images.s(), save_image.s(), get_image_files.s(), send_image.s()
    ).apply_async()

from __future__ import absolute_import,unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger

from .utils import save_latest_flickr_image

logger = get_task_logger(__name__)


@shared_task
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    
    logger.info("Saved image from Flickr")
    return save_latest_flickr_image()

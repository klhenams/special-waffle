from celery import shared_task
from celery.utils.log import get_task_logger

from .services.spreadsheet import Spreadsheet

logger = get_task_logger(__name__)


@shared_task()
def get_items():
    try:
        sp = Spreadsheet()
        sp.get_list()
        # logger.info(f"Task get items success: {results}")
    except Exception as err:
        logger.info(f"Task get items error: {err}")

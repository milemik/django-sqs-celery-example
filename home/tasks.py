from time import sleep

from celery import shared_task
from .utils import add_user_input


@shared_task
def first_celery_task(user_input: str) -> None:
    print("RUNNING TASK")
    sleep(5)
    add_user_input(user_input=user_input)
    print("TASK DONE")
    return 0


@shared_task
def send_message_to_sqs():
    print("SIMPLE MESSAGE")

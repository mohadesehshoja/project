from django.http import HttpResponse
import time
from core.celery import app
from celery import shared_task


@app.task
def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()


@shared_task
def my_task_2():
    file = open("test.txt", 'a')
    file.write("hello world ")
    file.close()


def home(request):
    my_task.delay()
    return HttpResponse("Hello, world. You're at the")

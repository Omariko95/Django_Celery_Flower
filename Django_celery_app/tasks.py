from __future__ import absolute_import
from celery import shared_task

#Let's utilize shared task decorator
@shared_task
def test(var):
    return 'The test task executed with argument "%s" ' % var
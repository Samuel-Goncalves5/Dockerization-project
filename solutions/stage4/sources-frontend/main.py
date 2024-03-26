from celery import Celery
from celery.result import AsyncResult
# Celery configuration (global)
CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]  # 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
CELERY_RESULT_BACKEND = os.environ["CELERY_RESULT_BACKEND"]  # 'rpc://'
# Initialize Celery
celeryapp = Celery(broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
celeryapp.config_from_object('celeryconfig')

# In some function, for task submission
def process_image_proxy(image):
    task_id = celeryapp.send_task('worker.process_image', args=(image,), serializer="pickle")
    generated_text = AsyncResult(task_id, app=celeryapp).get()
    return generated_text
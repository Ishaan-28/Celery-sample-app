from worker import process_task

# Submitting a task
task_data = {"message": "Hello, Celery!"}
process_task.delay(task_data)
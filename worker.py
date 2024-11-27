from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379')

app.conf.task_serializer = 'json'
app.conf.accept_content = ['json']
app.conf.task_ignore_result = True
app.conf.worker_send_task_events = True
app.conf.task_send_sent_event = True

@app.task
def process_task(task_data):
    print(f"Received task: {task_data}")

if __name__ == '__main__':
    app.worker_main(
        argv=[
            "worker",
            "--loglevel=info", 
            "--queues=queue-a10g-1",
            "--concurrency=1",
        ]
    )
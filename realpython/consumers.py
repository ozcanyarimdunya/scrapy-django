import json
from time import sleep

from channels.generic.websocket import WebsocketConsumer

from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')


class StatusConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, **kwargs):
        text_data = kwargs.get('text_data')
        text_data_json = json.loads(text_data)
        task_id = text_data_json['taskId']

        while True:
            status = scrapyd.job_status(project="default", job_id=task_id)
            dumps = json.dumps({'status': status})
            self.send(text_data=dumps)
            if dumps == "finished" or dumps == "":
                break

            sleep(2)

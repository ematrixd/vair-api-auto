from time import sleep

class Vair():

    def __init__(self, tasks):
        self.tasks = tasks

    def _check_task(self):
        state = 0
        message = ''
        while state == 0:
            sleep(10)
            task_id = self.tasks.swagger.task_id
            task_data = self.tasks.swagger.start_method(f'task_task_id', 'code', 'state', 'message', path=f'api/v2/task/{task_id}')
            for task in task_data:
                if task.get('code', False):
                    print(f'Выполняется задача: {task['code']}')
                if task.get('state', False):
                    state = task['state']
                if task.get('message', False):
                    message = task['message']
        print(message)

    def search(self):
        pass

    def get(self):
        pass

    def post(self):
        for task in self.tasks.all_data:
            for key, value in task.items():
                self.tasks.swagger.start_method(key, **value)
                self._check_task()

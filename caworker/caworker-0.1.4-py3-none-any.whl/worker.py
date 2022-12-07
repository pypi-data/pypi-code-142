import platform
import pycamunda.externaltask
import pycamunda.processinst
import pycamunda.task
import requests.auth
import requests.sessions
import envconfiguration as config


class Worker:

    def __init__(self):
        self.ENG_REST_URL = config.ENG_REST_URL
        self.HOST = platform.node()
        self.TOPIC = config.TOPIC
        self.WORKER_ID = self.HOST + self.TOPIC
        self.ENG_REST_USERNAME = config.ENG_REST_USERNAME
        self.ENG_REST_PASSWORD = config.ENG_REST_PASSWORD
        self.MAX_TASK_DURATION = config.MAX_TASK_DURATION
        self.SESSION = self.__get_auth(self.ENG_REST_USERNAME,
                                       self.ENG_REST_PASSWORD)

    def __get_auth(self, username, password):
        session = requests.sessions.Session()
        session.auth = requests.auth.HTTPBasicAuth(username=username,
                                                   password=password)
        return session

    def fetch_tasks(self, topic=None, max_tasks=1, lock_duration=30000):

        topic = self.TOPIC if topic is None else topic

        fetch_and_lock = pycamunda.externaltask.FetchAndLock(
            url=self.ENG_REST_URL,
            worker_id=self.WORKER_ID,
            max_tasks=max_tasks)

        fetch_and_lock.add_topic(name=topic, lock_duration=lock_duration)
        fetch_and_lock.session = self.SESSION

        try:
            resp = fetch_and_lock()
            if len(resp) > 0:
                print('Fetched {} tasks.'.format(len(resp)))
            return resp
        except ValueError:
            print('Featching and locking task failed.')
            return tuple()

    def complete_task(self, task_id, variables={}):
        complete = pycamunda.externaltask.Complete(url=self.ENG_REST_URL,
                                                   id_=task_id,
                                                   worker_id=self.WORKER_ID)
        complete.session = self.SESSION

        for variable in variables:
            complete.add_variable(name=variables[variable]['name'],
                                  value=variables[variable]['value'],
                                  type_=variables[variable]['type'] if 'type'
                                  in variables[variable] else 'string')

        try:
            return complete()
        except ValueError:
            print('Setting variables failed.')
            return None

    def getTask(self, process_instance_id):
        GetListTasks = pycamunda.task.GetList(
            url=self.ENG_REST_URL, process_instance_id=process_instance_id)

        GetListTasks.session = self.SESSION

        task_id = GetListTasks()[0].id_

        return task_id

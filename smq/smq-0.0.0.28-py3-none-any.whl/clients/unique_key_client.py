class UniqueKeyClient():

    def __init__(self, register_manager, topic_name):
        self._register_manager = register_manager
        self._topic_name = topic_name
        self._topic().bind(self._topic_name)

    def _topic(self):
        return self._register_manager.get_unique_key_topic()

    def send(self, key, data):
        qid = self._topic().put(self._topic_name, key, data)
        return qid

    def receive(self):
        data, qid = self._topic().get(self._topic_name)
        return data, qid

    def commit(self, qid):
        result = self._topic().ack(self._topic_name, qid)
        return result

    def send_batch(self, data_list: list):
        qid_list = self._topic().put_batch(self._topic_name, data_list)
        return qid_list

    def receive_batch(self, max_num):
        return self._topic().get_batch(self._topic_name, max_num)

    def commit_batch(self, qid_list):
        results = [self._topic().ack(self._topic_name, qid) for qid in qid_list]
        return results

    def rebind(self):
        self._register_manager.reconnect()
        self._topic().bind(self._topic_name)
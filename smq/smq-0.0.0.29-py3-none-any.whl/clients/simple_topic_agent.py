class SimpleTopicAgent:

    def __init__(self, register_topic, topic_name):
        self._topic_name = topic_name
        self._register_topic = register_topic
        self._register_topic.bind(topic_name)

    def send(self, data):
        qid = self._register_topic.put(self._topic_name, data)
        return qid

    def receive(self):
        data, qid = self._register_topic.get(self._topic_name)
        return data, qid

    def commit(self, qid):
        result = self._register_topic.ack(self._topic_name, qid)
        return result

    def send_batch(self, data_list: list):
        qid_list = self._register_topic.put_batch(self._topic_name, data_list)
        return qid_list

    def receive_batch(self, max_num):
        return self._register_topic.get_batch(self._topic_name, max_num)

    # def receive_batch(self, max_num):
    #     datas = []
    #     for i in range(max_num):
    #         data, qid = self._register_topic.get(self._topic_name)
    #         if data is None:
    #             break
    #         datas.append((data, qid))
    #     return datas

    # def receive_batch(self, num):
    #     datas = [self._register_topic.get(self._topic_name) for i in range(num)]
    #     return datas

    def commit_batch(self, qid_list):
        results = [self._register_topic.ack(self._topic_name, qid) for qid in qid_list]
        return results

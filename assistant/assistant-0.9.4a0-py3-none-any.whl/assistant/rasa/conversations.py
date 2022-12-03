import pickle

from assistant import ASSISTANT_PATH

class Conversations:
    def __init__(self):
        self.history = {}
        self.conversations = {}
        self.db_path = f"{ASSISTANT_PATH}/db"
    
    def add_conversation(self, user, messenger, message, timestamp):
        m = {}
        if messenger in ['user', user]:
            m['messenger'] = 'user'
        elif messenger in ['agent', 'assistant']:
            m['messenger'] = 'agent'
        else:
            raise InvalidMessengerError(messenger, user)
        
        m['message'] = message
        m['timestamp'] = timestamp
        
        if not self.get_conversation(user):
            self.conversations[user] = []
        
        self.conversations[user].append(m)
        
        return self.get_conversation(user)
    
    def get_conversation(self, user):
        return self.conversations.get(user, [])

    def archive_conversation(self, user):
        c = self.get_conversation(user)
        if c:
            if not self.history.get(user, []):
                self.history[user] = []
            self.history[user].append(c)
            self.conversations[user] = []
            self.update_archive(user)
    
    def get_history(self, user):
        return self.history.get(user, self.load_archive(user))
    
    def load_archive(self, user):
        f = f"{self.db_path}/{user}"
        if os.path.exists(f):
            d = pickle.load(f)
            h = d.get('history', [])
            self.history[user] = h
            return h
        else:
            return []

    def save_archive(archive, user):
        p = f"{self.db_path}/{user}"
        if os.path.exists(p):
            with open(p, 'r') as rf:
                a = pickle.load(p)
        else:
            a = {}
        a['history'] = archive
        with open(p, 'w') as wf:
            pickle.dump(a, p)

    def update_archive(self, user):
        save_archive(self.get_history(user), user)
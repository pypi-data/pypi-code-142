import requests

from prompt_toolkit.completion import Completion, Completer
from prompt_toolkit.document import Document

class BERTCompleter(Completer):

	def predict_next_words(self, current_words, host="localhost", port="5068"):
		try:
			headers = {'content-type': 'application/json'}
			payload = { 'text': current_words }
			r = requests.post(f"http://{host}:{port}/api/v1/predict", json=payload, headers=headers)
			if r.status_code == 200:
				rj = r.json()
				if rj:
					return rj.get('prediction', [])
		except (ConnectionError, Exception) as e:
			pass #print(e) # No need to make a fuss about it
		return []

	def get_completions(self, document, complete_event):
		word_before_cursor = document.get_word_before_cursor()
		for word in self.predict_next_words(word_before_cursor):
			yield Completion(word, -len(word_before_cursor))




word_completer = BERTCompleter()
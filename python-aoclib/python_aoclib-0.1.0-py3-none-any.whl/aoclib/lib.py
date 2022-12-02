import requests
import time
from load_config import getSessionID

class AOC:
    def __init__(self, year: int, date: int, session: str = '') -> None:
        if not session:
            self.sessionID = getSessionID()
        else:
            self.sessionID = session

        self.session = requests.Session()
        self.session.cookies.set({'session': self.sessionID})

        self.year = year
        self.date = date
        self.base_url = f'https://adventofcode.com/{str(self.year)}/day/{str(self.date)}'

    def getdata(self) -> str:
        url = self.base_url + '/input'
        response = self.session.get(url)

        if response.status_code == 200:
            return str(response.content).splitlines()
        else:
            raise Exception('Cannot fetch input data')

    def submit(self, level: int, output: str) -> str:
        url = self.base_url + '/answer'
        
        if level not in [1, 2]:
            raise Exception('Current level is not 1 or 2')

        payload = {
            'level': str(level),
            'answer': output
        }

        response = self.session.post(url, data = payload)

        if response.status_code != 200:
            raise Exception('Non-200 status code when submitting')

        result_text = response.text
        verdict = ''
        retry = False

        if "That's the right answer" in result_text:
            verdict = 'ACCEPTED!'
        elif "That's not the right answer" in result_text:
            verdict = 'WRONG ANSWER...'
        elif "Did you already complete it" in result_text:
            verdict = 'ALREADY DONE.'
        elif 'You gave an answer too recently' in result_text:
            verdict = 'WAIT 30s BEFORE RETRYING...'

        print(f'{str(self.year)}-12-{str(self.date)}: {verdict}')

        if retry:
            time.sleep(30)
            submit(level, output)

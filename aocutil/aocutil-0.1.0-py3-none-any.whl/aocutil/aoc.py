#!/usr/bin/env python3

import logging
import datetime
from pathlib import Path
import textwrap

import os.path
import re
from typing import AnyStr, Sequence, OrderedDict, Optional

import requests
from urllib.parse import urljoin

from pyquery import PyQuery


class Aoc:
    def __init__(self, year: Optional[int] = None, day: Optional[int] = None, session_id: Optional[str] = None):
        if session_id is not None:
            self.session_id = session_id
        else:
            logging.debug("No session id given trying to read from config")
            config_path: Path = Path.home().joinpath(".config", "aocutil", "session_id")
            logging.debug(f"Looking for session id in config file [{config_path}]")
            if config_path.exists() and config_path.is_file():
                self.session_id = config_path.read_text().strip()
            else:
                logging.critical(f"Config file [{config_path}] for session id not found")
                raise RuntimeError("No session id provided")
        logging.debug(f"Session id: {self.session_id}")

        if year is not None:
            self.year = year
        else:
            logging.debug(f"No year given trying to guess year")
            current_date = datetime.datetime.now()
            self.year = current_date.year
        logging.debug(f"Year: {self.year}")

        if day is not None:
            self.day = day
        else:
            logging.debug(f"No day given trying to guess day")
            current_date = datetime.datetime.now()
            self.day = current_date.day
        logging.debug(f"Day: {self.day}")

        self.base_url = f"https://adventofcode.com/{self.year}/day/{self.day}/"
        logging.debug(f"Base url: {self.base_url}")

        self.cookie = {'session': self.session_id}

    def input(self):
        return AocInput(urljoin(self.base_url, "input"), f"{self.year}_{self.day}", self.cookie)

    def submit(self, answer, level=None):
        if level is None:
            logging.debug(f"No level given trying to guess")
            resp = requests.get(url=self.base_url[:-1], cookies=self.cookie)
            d = PyQuery(resp.content)
            p = d('main > form > input:hidden')
            if p:
                level = p.attr("value")
                logging.debug(f"Setting level to {level}")

        logging.debug(f"Guessed: {answer}")
        input(f"Puzzle: {self.year}-{self.day}\nAnswer: {answer}\nLevel: {level}\nSubmit? ")

        url = urljoin(self.base_url, "answer")
        resp = requests.post(url=url, data={'level': level, 'answer': answer}, cookies=self.cookie)

        d = PyQuery(resp.content)
        p = d('main > article')

        print()
        if p.text():
            print(textwrap.fill(p.text()))
        else:
            print(textwrap.fill(d.text()))


class AocInput:
    def __init__(self, url, name, cookie):
        self.url = url
        self.name = name
        self.cookie = cookie

    def content(self):
        if os.path.exists(self.name):
            with open(self.name) as f:
                return f.read()
        else:
            content = requests.get(url=self.url, cookies=self.cookie).text
            with open(self.name, 'w') as f:
                f.write(content)
            return content

    def read(self) -> AnyStr:
        return self.content()

    def lines(self) -> Sequence[AnyStr]:
        return self.content().splitlines()

    def parse(self, token: OrderedDict[AnyStr, AnyStr]):
        lines = self.lines()
        tokenized_lines = []
        for line in lines:
            line_tokens = {}
            for k, v in token.items():
                pat = re.compile(v)
                m = pat.match(line)
                line = line[m.end():]
                if not k.startswith("_"):
                    line_tokens[k] = m.group()

            tokenized_lines.append(line_tokens)
        return tokenized_lines

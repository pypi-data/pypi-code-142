#!/usr/bin/env python
__version__=1.6
HEADLINE="""
    ___              _      __              __ 
   /   |  __________(_)____/ /_____ _____  / /_
  / /| | / ___/ ___/ / ___/ __/ __ `/ __ \/ __/
 / ___ |(__  |__  ) (__  ) /_/ /_/ / / / / /_  
/_/  |_/____/____/_/____/\__/\__,_/_/ /_/\__/  
"""

#import tqdm

import threading
import os
import pickle
import time
import logging
import random
import json, toml
import socket
import functools
import psutil
import glob
#import subprocess

from prompt_toolkit import PromptSession
from prompt_toolkit.application import get_app
from prompt_toolkit.formatted_text import (
	HTML,
	fragment_list_width,
	merge_formatted_text,
	to_formatted_text,
)
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.shortcuts import CompleteStyle, set_title, clear, confirm
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory
from datetime import datetime
from halo import Halo
from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path


try:
	wxh = os.get_terminal_size()
	is_terminal_simulated = False
	WIDTH = int( wxh.columns )
	HEIGTH = int( wxh.lines )
except OSError as ose:
	wxh = None
	is_terminal_simulated = True
	WIDTH = 0
	HEIGTH = 0



CONV = []

AGENT_NAME = "Assistant"
GREETINGS = "Bonjour! Ravis de vous revoir si vite."
LOGNAME = os.environ.get('LOGNAME', 'anymus')
SETTINGS_PATH = glob.glob(f'/home/*/.assistant/settings.tml')[0]
ASSISTANT_PATH = Path(f"{SETTINGS_PATH.replace('/settings.tml', '')}").resolve().as_posix()
HOME = Path(f"{ASSISTANT_PATH}/..").resolve().as_posix()
USERNAME = os.environ.get('USERNAME', HOME.replace("/home/", "") )


I18N, L10N = (x for x in os.environ.get('LANG', "en_EN.UTF-8").split(".")[0].split("_"))

HISTORY_FILEPATH = HOME + "/.history"

STYLE=Style.from_dict(
	{
		"username": "#aaaaaa bold",
		"path": "#ffffff bold",
		#"branch": "bg:#666666",
		#"branch exclamation-mark": "#ff0000",
		#"env": "bg:#666666 bold",
		#"left-part": "bg:#444444",
		#"right-part": "bg:#444444",
		#"padding": "bg:#444444",
		"wallet": "#0476D0",
		"bottom_toolbar": 'noreverse black bg:orange'
	}
)


def load_settings():
	with open(SETTINGS_PATH, 'r') as f:
		SETTINGS = toml.load(f)
		f.close()
		return SETTINGS

def get_is_speech_autorized():
	SETTINGS = load_settings()
	return True if SETTINGS['tts'].get('is_allowed_speaking', "false").lower() == "true" else False

def get_is_speech_recognition_enabled():
	SETTINGS = load_settings()
	return True if SETTINGS['stt'].get('is_allowed_listening', "false").lower() == "true" else False


def set_is_speech_recognition_enabled(is_speech_recognition_enabled: bool):
	fr = open(SETTINGS_PATH, 'r')
	SETTINGS = toml.load(fr)
	fr.close()

	SETTINGS['stt']['is_allowed_listening'] = "true" if is_speech_recognition_enabled == True else "false"

	fw = open(SETTINGS_PATH, 'w')
	toml.dump(SETTINGS, fw)
	fw.close()

	return is_speech_recognition_enabled

def set_is_speech_autorized(is_speech_autorized: bool):
	fr = open(SETTINGS_PATH, 'r')
	SETTINGS = toml.load(fr)
	fr.close()

	SETTINGS['tts']['is_allowed_speaking'] = "true" if is_speech_autorized == True else "false"

	fw = open(SETTINGS_PATH, 'w')
	toml.dump(SETTINGS, fw)
	fw.close()

	return is_speech_autorized

is_speech_autorized = get_is_speech_autorized()
is_speech_recognition_enabled = get_is_speech_recognition_enabled()

def checkIfProcessRunning(processName):
	'''
	Check if there is any running process that contains the given name processName.
	'''
	#Iterate over the all the running process
	for proc in psutil.process_iter():
		try:
			# Check if process name contains the given name string.
			if processName.lower() in proc.name().lower():
				return True
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return False



def now():
	return datetime.now()

def load_history():
	try:
		with open(HISTORY_FILEPATH, 'rb') as f:
			history = pickle.load(f)
			f.close()
			return history
	except Exception as e:
		return []

def dump_history(history):
	with open(HISTORY_FILEPATH, 'wb') as f:
		pickle.dump(history, f)
		f.close()

def get_last_timestamp_from(history):
	if history != []:
		last_converstation = history[-1]
		if last_converstation:
			last_utterance = last_converstation[-1]
			if last_utterance:
				last_timestamp = last_utterance.get('timestamp')
				return last_timestamp
	
	last_timestamp = None
	return last_timestamp

def no_current_conversation_from(history):
	number_of_minutes_afterwhich_the_last_conversation_is_no_longer_the_current_one_anymore = 3
	last_timestamp = get_last_timestamp_from(history)
	if last_timestamp != None:
		n = now()
		if ( ( n - last_timestamp ).total_seconds() / 60.0 ) < number_of_minutes_afterwhich_the_last_conversation_is_no_longer_the_current_one_anymore:
			return False
	return True

def get_current_conversation_from(history):
	if no_current_conversation_from(history):
		is_created = True
		current_conversation = []
	else:
		is_created = False
		current_conversation = history[-1]
	return current_conversation, is_created

def save_conversation(conversation, history, is_created=True):
	if is_created:
		history.append(conversation)
	else:
		history[-1] = conversation
	dump_history(history)

def journalize(utterance, timestamp=None, character="assistant", context=dict(os.environ)):
	try:
		if timestamp == None:
			timestamp = now()
		
		journal_entry = {
			'timestamp': timestamp,
			'utterance': utterance,
			'character': character,
			'context': context
		}
		history = load_history() # [ #this is a list of all conversations
		current_conversation, is_created = get_current_conversation_from(history) # [ #this is a list of utterances inside a conversation
		current_conversation.append(journal_entry)
		CONV.append(journal_entry)
		save_conversation(current_conversation, history, is_created=is_created)
	except Exception as e:
		print("Error in journalize")
		print(e)

def fetch_conv_from_history():
	history = load_history() # [ #this is a list of all conversations
	current_conversation, is_created = get_current_conversation_from(history) # [ #this is a list of utterances inside a conversation
	return current_conversation

def centered(string_lines):
	total_width = WIDTH #get_app().output.get_size().columns
	centered_string_lines = ""

	for l in string_lines.split("\n"):
		centered_string_lines += l.center(total_width) + "\n"

	return centered_string_lines

def right_aligned(string_lines):
	total_width = WIDTH #get_app().output.get_size().columns
	centered_string_lines = ""

	for l in string_lines.split("\n"):
		centered_string_lines += l.rjust(int(total_width)) + "\n"

	return centered_string_lines

def print_banner():
	clear
	for l in HEADLINE.split("\n"):
		print_formatted_text(HTML('<orange>'+ centered(l) + '</orange>'), end="")
	print("\n")

def user_say(utterance):
	to_print = "\t%s" % utterance
	print("")
	print_formatted_text(HTML('<grey>'+ to_print + '</grey>'))
	CONV.append(to_print)

def agent_say(utterance, margin="\t"):
	to_print = "%s%s\n" % (margin, "\n\n \t".join(utterance.split('\n')))
	print("")
	print_formatted_text(HTML('<orange>'+ to_print + '</orange>'))
	CONV.append(to_print)

def print_history():
	utterances = fetch_conv_from_history()
	for u in utterances:
		if u.get('character') == "assistant":
			if u.get('utterance'):
				agent_say(u.get('utterance'))
		else:
			if u.get('utterance'):
				user_say(u.get('utterance'))

def bottom_toolbar():
	return HTML(
		"<bottom_toolbar>" + centered("[Q]uit | Toogle [S]peech Services | Toogle [L]istening Services | [E]dition mode").replace("\n", "") + "</bottom_toolbar>"
	)
		
def get_prompt() -> HTML:
	"""
	Build the prompt dynamically every time its rendered.
	"""
	PWD = get_pwd() #too cpu hungry
	_margin = "        "
	type_now = "You can now type something"
	tool_tip = HTML("<darkgrey>%s%s</darkgrey>" % (_margin, type_now))
	left_part = HTML(
		"<left-part>"
		"<env>        <orange></orange>  %s %s</env> "
		"<path>%s</path>"
		"</left-part>"
	) % ("" if not is_speech_recognition_enabled else "<orange></orange>", "ﰝ" if not is_speech_autorized else "<orange>ﰝ</orange>", PWD.replace("/home/%s" % USERNAME, " "),)
	right_part = HTML(
		"<right-part> "
		#"<branch> \uF489 <exclamation-mark>\uE20E</exclamation-mark> </branch> "
		" <wallet>\uF219  %s</wallet> "
		" <username>%s        </username> "
		"</right-part>"
	) % ("0.00", USERNAME)

	used_width = sum(
		[
			fragment_list_width(to_formatted_text(left_part)),
			fragment_list_width(to_formatted_text(right_part)),
		]
	)

	total_width = WIDTH
	padding_size = total_width - used_width

	padding = HTML("<padding>%s</padding>") % (" " * padding_size,)
	
	return merge_formatted_text([tool_tip, "\n", left_part, padding, right_part, "\n", "        "])

def prompt() -> str:
	try:
		set_title(AGENT_NAME)

		history = FileHistory(filename=HOME+"/.assistant/history.pkl")

		session = PromptSession(
			history=history,
			auto_suggest=AutoSuggestFromHistory(),
			enable_history_search=True,
			enable_system_prompt=True,
			style=STYLE
		)

		completer_list = []
		completer_meta_dict = {}
		intent_map = {}


		completer = FuzzyWordCompleter(
			completer_list,
			meta_dict=completer_meta_dict,
			#ignore_case=True,
		)

		return session.prompt(
				get_prompt,
				refresh_interval=1,
				completer=completer,
				complete_style=CompleteStyle.READLINE_LIKE,
				bottom_toolbar=bottom_toolbar
			)
	except KeyboardInterrupt:
		# Ctrl-C pressed.
		return
	except Exception as e:
		raise e

def get_env():
	try:
		with open(f'{ASSISTANT_PATH}/.env', 'rb') as f:
			env = pickle.load(f)
			f.close()
			return env
	except FileNotFoundError as f:
		return {}

def save_env(env):
	with open(f'{ASSISTANT_PATH}/.env', 'wb') as f:
		pickle.dump(env, f)
		f.close()
	return env

def set_env(key: str, val: str):
	env = get_env()
	env[key] = val
	env = save_env(env)
	return env

def get_pwd():
	env = get_env()
	return env.get('PWD', os.environ.get('PWD', HOME))

PWD = get_pwd()

def say(text, language="en", host="localhost", port=15553):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	req = {
		'text': str(text),
		'lang': str(language)
	}
	req_b = json.dumps(req).encode('utf-8', 'ignore')
	s.send(req_b)
	r = s.recv(1024).decode('utf-8', 'ignore')
	s.close()
	_wav = AudioSegment.from_wav(file=r)
	play(_wav)
	os.remove(r)
	return text

def main(ARGS):
	try:
		if ARGS.autorize_speech:
			is_speech_autorized = ARGS.autorize_speech
		else:
			is_speech_autorized = True if checkIfProcessRunning('think') and get_is_speech_autorized() else False
		
		if ARGS.host:
			HOST = ARGS.host
		if ARGS.port:
			PORT = ARGS.port
		if ARGS.interactive:
			# > assistant -i [ ]
			_interactive = True
		else:
			_interactive = False

		if ARGS.version:
			_text = [
				"Vous utilisez Assistant version " + str(__version__) + ".",
			]
			_show_version = True
			_enable_interpretation = True
			_disable_interpretation = False
			_no_newline = False
			for _t in _text:
				print(_t)
				if is_speech_autorized:
					say(_t, I18N)
			return __version__

		elif ARGS.command:
			set_env('PWD', get_pwd())
			if get_is_speech_recognition_enabled == False and ARGS.spoken: # I know this sounds like out of nowhere but basically this tells assistant: if you listen something while you are not allowed to listen, forget what you eard.
				return
			
			# > assistant [ -c 'command' ]
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((HOST, PORT))
			query = str(ARGS.command)
			# add command to history
			journalize(query, character=LOGNAME)

			# answer command
			req = {
				'query': query,
				'lang': I18N,
				'spoken': ARGS.spoken,
				'credential': USERNAME
				}
			req_b = json.dumps(req).encode('utf-8', 'ignore')
			s.send(req_b)
			r = json.loads(s.recv(1024))
			s.close()
			response = r.get('answer', None)
			if response:
				journalize(str(response), character="assistant")
				print(str(response))
				if get_is_speech_autorized and checkIfProcessRunning('think'):
					say(str(response), I18N)
			return
		elif ARGS.standard_input:
			# > echo "command" | assistant -s
			print("Standard input is not yet accepted")
		elif ARGS.script2exec:
			# > assistant ( [ script [ args ... ] ] | [ COMMAND [...] ] )
			# if script is valid script?
				# answer script with arguments
			# else
				# answer script with arguments as command
			pass
		else:
			# > assistant
			# Start an interactive assistant session
			if LOGNAME.lower() != USERNAME.lower():
				print("Assistant: Running assistant as root in interactive mode is forbidden.")
				print("As asking something to Assistant is already like running a command as root.")
				print("")
				print("Assistant: Either you don't know what you are doing.")
				print("In which case I recommend you run `assistant` as yourself insead of as root.")
				print("")
				print("Assistant: Or you know exactly what you are doing and you are trying to run Assistant by the system.")
				print("If this is your case; try using the --command (-c) flag instead of interactive mode.")
				print("(e.g):\tsudo assistant -c 'Thanks for the tip.'")
				return
				
			if not is_terminal_simulated:
				set_env('PWD', os.environ.get('PWD', get_pwd()))
				is_speech_autorized = True if checkIfProcessRunning('think') else False
				spinner = Halo(spinner='dots')
				clear()
				print_banner()
				current_conv = fetch_conv_from_history()
				if current_conv:
					print_history()
				else:
					spinner.start()
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.connect((HOST, PORT))
					GREETINGS_REQUEST = f":n --{I18N}"
					req = {
						'query': GREETINGS_REQUEST, #This initialize the model for a new conversation (aka the assistant says something nice when you login)
						'lang': I18N,
						'spoken': ARGS.spoken,
						'credential': USERNAME
						}
					req_b = json.dumps(req).encode('utf-8', 'ignore')
					s.send(req_b)
					r = json.loads(s.recv(1024))
					s.close()
					spinner.stop()
					response = r.get('answer', None)
					if response:
						GREETINGS = response
						agent_say(GREETINGS)
						journalize(GREETINGS)
						if get_is_speech_autorized and checkIfProcessRunning('think'):
							say(GREETINGS, I18N)
				try:
					while True:
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.connect((HOST, PORT))
						query = prompt()    
						journalize(query, character=USERNAME)
						if query in ['clear', 'cls', 'clear all', 'clear screen']:
							history = load_history()
							conversation = []
							save_conversation(conversation, history, is_created=False)
							clear()
							print_banner()
							spinner.start()
							s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
							s.connect((HOST, PORT))
							GREETINGS_REQUEST = f":n --{I18N}"
							req = {
								'query': GREETINGS_REQUEST, #This initialize the model for a new conversation (aka the assistant says something nice when you login)
								'lang': I18N,
								'spoken': ARGS.spoken,
								'credential': USERNAME
								}
							req_b = json.dumps(req).encode('utf-8', 'ignore')
							s.send(req_b)
							r = json.loads(s.recv(1024))
							s.close()
							spinner.stop()
							response = r.get('answer', None)
							if response:
								GREETINGS = response
								agent_say(GREETINGS)
								journalize(GREETINGS)
								if get_is_speech_autorized and checkIfProcessRunning('think'):
									say(GREETINGS, I18N)
						elif query in ['l', 'L']:
							is_speech_recognition_enabled = not is_speech_recognition_enabled
							if is_speech_recognition_enabled:
								try:
									assert checkIfProcessRunning('ear') != False
									#os.environ['ASSISTANT_ALLOWED_LISTENING'] = "true"
									set_is_speech_recognition_enabled(True)
								except AssertionError as ae:
									is_speech_recognition_enabled = False
									#os.environ['ASSISTANT_ALLOWED_LISTENING'] = "false"
									set_is_speech_recognition_enabled(False)
							else:
								#os.environ['ASSISTANT_ALLOWED_LISTENING'] = "false"
								set_is_speech_recognition_enabled(False)
						elif query in ['s', 'S']:
							is_speech_autorized = not get_is_speech_autorized()
							if is_speech_autorized:
								try:
									assert checkIfProcessRunning('think')
								except AssertionError as ae:
									is_speech_autorized = False
							set_is_speech_autorized(is_speech_autorized)
						elif query not in ['stop', 'exit', 'quit', 'q', 'Q', ":q", ':wq', '/q', None]:
							clear()
							print_banner()
							print_history() 
							spinner.start()
							req = {
								'query': str(query),
								'lang': I18N,
								'spoken': ARGS.spoken,
								'credential': USERNAME
								}
							req_b = json.dumps(req).encode('utf-8', 'ignore')
							s.send(req_b)
							r = json.loads(s.recv(1024))
							s.close()
							response = r.get('answer', None)
							if response:
								journalize(response, character="assistant")
								spinner.stop()
								agent_say(response)
							else:
								spinner.stop()
								print()
						else:
							spinner.start()
							s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
							s.connect((HOST, PORT))
							EXIT_REQUEST = ":q --%s" % I18N
							req = {
								'query': str(EXIT_REQUEST), #This initialize the model for a new conversation (aka the assistant says something nice when you login)
								'lang': I18N,
								'spoken': ARGS.spoken,
								'credential': USERNAME
								}
							req_b = json.dumps(req).encode('utf-8', 'ignore')
							s.send(req_b)
							r = json.loads(s.recv(1024))
							s.close()
							spinner.stop()
							response = r.get('answer', None)
							if response:
								GREETINGS = response
								agent_say(GREETINGS)
								journalize(GREETINGS)
								if get_is_speech_autorized and checkIfProcessRunning('think'):
									say(GREETINGS, I18N)
							return
				
				except KeyboardInterrupt as q:
					return
				
				except Exception as e:
					print("Error while interactive session")
					raise e
			else:
				# If you end up here you are trying to access an interactive session without an interactive terminal
				print("Assistant: Interactive session has been disabled since terminal emulator is simulated.")
				print("OSError: [Errno 25] Inappropriate ioctl for device")
				print("")
				print("Assistant: Either you don't know what you are doing.")
				print("In which case I recommend you open a graphical terminal emulator such as gnome-terminal and type `assistant` to open an interactive session.")
				print("")
				print("Assistant: Or you know exactly what you are doing and you are trying to use Assistant on a simulated terminal emulator.")
				print("If this is your case; try using the --command (-c) flag instead of interactive mode.")
				print("(e.g):\tassistant -c 'Thanks for the tip.'")

	except Exception as err:
		print("Error in main")
		raise err



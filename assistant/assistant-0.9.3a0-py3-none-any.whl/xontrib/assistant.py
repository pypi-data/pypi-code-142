import xonsh
import questionary
from prompt_toolkit.shortcuts import clear, set_title
#from assistant import conditions
from assistant.ptk_shell.shell import AssistantShell

__all__ = ()

set_title("Assistant")
clear()
print("Hi.")
print("My name is Assistant.")
print()
print("Before we begin, I have a few questions:")
print()

def is_username_really_user_lastname(username: str = __xonsh__.env.get('USERNAME')):
	q = questionary.confirm(f"Is `{username.capitalize()}` really your lastname ?", default=False).ask()
	if q is None:
		raise KeyboardInterrupt()
	return q	

def what_is_user_lastname():
	q = questionary.text("Then what is your lastname ?").ask().lower()
	if q is None:
		raise KeyboardInterrupt()
	return q

def what_is_user_firstname(user):
	q = questionary.text(f"So {user.capitalize()}, what is your firstname ?").ask().lower()
	if q is None:
		raise KeyboardInterrupt()
	return q

def what_is_user_gender():
	q = questionary.select(
		"Which option fit you the most ?",
		choices=["male", "female", "none"],
	).ask()
	if q is None:
		q = "none"
	return q

def what_is_user_surname(surname: str = __xonsh__.env.get('USERNAME')):
	print()
	print(f"( enter multiple values by using commas. )")
	q = questionary.text("How shall I call you,", default=surname).ask()
	if q is None:
		raise KeyboardInterrupt()
	return q

try:
	is_first_time = False
	if not __xonsh__.env.get('USER_LASTNAME'):
		__xonsh__.env['USER_LASTNAME'] = __xonsh__.env.get('USERNAME') if is_username_really_user_lastname() else what_is_user_lastname()
		is_first_time = True
	if not __xonsh__.env.get('USER_FIRSTNAME'):
		__xonsh__.env['USER_FIRSTNAME'] = what_is_user_firstname(__xonsh__.env.get('USER_LASTNAME', __xonsh__.env.get('USERNAME')))
		is_first_time = True
	if is_first_time:
		print()
		print(f"Very well, {__xonsh__.env.get('USER_FIRSTNAME').capitalize()} {__xonsh__.env.get('USER_LASTNAME').capitalize()}. Nice to meet you!")
	if not __xonsh__.env.get('USER_GENDER'):
		__xonsh__.env['USER_GENDER'] = what_is_user_gender()
		is_first_time = True
	if not __xonsh__.env.get('USER_SURNAME'):
		_surname = "Sir" if __xonsh__.env.get('USER_GENDER') == "male" else "My Lady" if __xonsh__.env.get('USER_GENDER') == "female"  else __xonsh__.env.get('USERNAME').capitalize()
		__xonsh__.env['USER_SURNAME'] = what_is_user_surname(_surname).replace(", ", ",").split(",")
		print(f"Very well, {__xonsh__.env.get('USER_SURNAME')[-1].capitalize()}.")
	
	print()
	print("Shall we get to business ?")
	
except KeyboardInterrupt:
	print("[Ctrl] + [C]: Exit")
	exit(130) #SIGTERM
except Exception as e:
 	raise e
 	print("Assistant: Error while loading from xontrib")
 	exit(e.exit_code)
#try:

__xonsh__.shell.shell = AssistantShell(execer=__xonsh__.shell.execer, ctx=__xonsh__.shell.ctx)

# 	__xonsh__.env['ASSISTANT_NLP_HOST'] = __xonsh__.env.get('ASSISTANT_NLP_HOST', 'localhost')
# 	__xonsh__.env['ASSISTANT_NLP_PORT'] = __xonsh__.env.get('ASSISTANT_NLP_PORT', '5005')



# 	if not conditions.is_nlp_server_up():
# 		# NLP server is not up !
# 		# We should start it now.
# 		USER = __xonsh__.env.get('USER', None)

# 		if not USER:
# 			print("Who are you?")
# 			exit()

# 		__xonsh__.env['ASSISTANT_PATH'] = __xonsh__.env.get('ASSISTANT_PATH', f'/home/{__xonsh__.env.get("USER")}/.assistant')
# 		__xonsh__.env['ASSISTANT_NLP_MODELS_PATH'] = __xonsh__.env.get('ASSISTANT_NLP_MODELS_PATH', f'{ASSISTANT_PATH}/models/{I18N}/NLU')

# 		# Load Domains

# 		if not __xonsh__.subproc_captured_stdout(['which', 'dmt']):
# 			dmt_repo = "https://gitlab.com/waser-technologies/technologies/dmt"
# 			__xonsh__.subproc_captured_stdout(['xpip', 'install', f'git+{dmt_repo}'])

# 		from domain.management import tools as dm_tools

# 		dm_tools.mk_assistant_dir(ASSISTANT_PATH)
# 		domains_path = f"{ASSISTANT_PATH}/domains/{I18N}"
# 		list_installed_domains = dm_tools.get_list_installed_domains(domains_path)

# 		if not list_installed_domains:
# 			__xonsh__.subproc_captured_stdout(['dmt', '-a', 'https://gitlab.com/waser-technologies/data/nlu/{I18N}/smalltalk.git'])
# 			__xonsh__.subproc_captured_stdout(['dmt', '-a', 'https://gitlab.com/waser-technologies/data/nlu/{I18N}/system.git'])

# 			if __xonsh__.subproc_captured_stdout(['dmt', '-V']):
# 				__xonsh__.subproc_captured_stdout(['dmt', '-T'])
# 			else:
# 				print("Error while training")
		
# 		# Prepare services
		
# 		# Load RASA Actions
# 		if not __xonsh__.subproc_captured_stdout(['systemctl', 'status', f'rasa.action.service']):
# 			__xonsh__.subproc_captured_stdout(['systemctl', 'enable', '--now', f'rasa.action.service'])
# 		# Load RASA models from services
# 		if not __xonsh__.subproc_captured_stdout(['systemctl', 'status', f'rasa.{I18N}.service']):
# 			__xonsh__.subproc_captured_stdout(['systemctl', 'enable', '--now', f'rasa.{I18N}.service'])
# 	else:
# 		# NLP server is up for work! 
# 		pass
# except KeyboardInterrupt:
# 	exit(130) #SIGTERM
# except Exception as e:
# 	raise e
# 	print("Assistant: Error while loading from xontrib")
# 	exit(e.exit_code)


# Enter the interactive shell
# assistant

# Good start! Get more documentation -> https://xon.sh/contents.html#guides


# Note! If you will write the xontrib on Python it will work faster 
# until https://github.com/xonsh/xonsh/issues/3953 hasn't released yet.
# To use Python:
#  1. rename this file from `xsh` to `py`
#  2. replace `xsh` to `py` in `setup.py`
#  3. rewrite the code using xonsh Python API i.e.:
#   * `__xonsh__.env.get('VAR', 'default')` instead of `${...}.get('VAR', 'default')`
#   * `__xonsh__.subproc_captured_stdout(['echo', '1'])` instead of `$(echo 1)`

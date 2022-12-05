import pathlib

from clickactions import Actions, Action, ActionState

actions = Actions(pathlib.Path.cwd(), 'DEBUG')

actions.logger.info("some info message")

action_state = ActionState(pathlib.Path.cwd() / 'TestAction')


class TestAction(Action):
    pass


test_action = TestAction(actions=actions, state=action_state)

test_action.logger.debug('From test action')

# -* UTF-8 *-
'''
==============================================================
@Project -> File : rlcard -> test_uno.py
@Author : yge
@Date : 2022/12/7 15:59
@Desc :

==============================================================
'''
import rlcard
from rlcard.agents import RandomAgent

env = rlcard.make("uno",config={"game_num_players":4})

print("Number of actions:", env.num_actions)
print("Number of players:", env.num_players)
print("Shape of state:", env.state_shape)
print("Shape of action:", env.action_shape)
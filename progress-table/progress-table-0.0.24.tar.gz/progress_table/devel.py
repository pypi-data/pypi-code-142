import random
import time

from colorama import Fore

from progress_table import ProgressTable

# %%

progress = ProgressTable(columns=["step", "x", "x squared"], num_decimal_places=10,
                         print_row_on_update=False)
progress.add_column("x root", color="green", width=12)

for step in range(3):
    progress["step"] = step  # insert step value in the current row

    for _ in progress(range(10)):  # display progress bar
        progress["x"] = 1
        time.sleep(0.1)  # simulate artificial work

    x = random.randint(0, 200)
    progress["x"] = x
    progress["x squared"] = x ** 2
    progress["x root"] = x ** 0.5
    progress.next_row()

progress.close()

# export your data
data = progress.to_list()
pandas_df = progress.to_df()
np_array = progress.to_numpy()

# %%

progress = ProgressTable(columns=["step", "x", "x squared"], num_decimal_places=10)
progress.add_column("x root", color=Fore.RED, width=12)

for step in progress(range(3)):
    progress["step"] = step  # insert step value in the current row

    for _ in range(10):  # display progress bar
        progress["x"] = 1
        time.sleep(0.1)  # simulate artificial work

    x = random.randint(0, 200)
    progress["x"] = x
    progress["x squared"] = x ** 2
    progress["x root"] = x ** 0.5
    progress.next_row()

progress.close()

# export your data
data = progress.to_list()
pandas_df = progress.to_df()
np_array = progress.to_numpy()


import random
import time

def surround_jumble(text, length=5, amt=1, wait=0, glitch=False, glitch_amt=5):
	for i in range(length):
		if glitch:
			num_txt = random.randint(1, 2)
			if num_txt == 1:
				jumble = random.choice(":;[]|!@#$%^&*()_+-=<>,./?}{      ") * random.randint(0, glitch_amt)
				time.sleep(wait+1/random.randint(1, 5)*5/random.randint(30, 100))
			else:
				jumble = random.choice(":;[]|!@#$%^&*()_+-=<>,./?}{      ") * amt
		else:
			jumble = random.choice(":;[]|!@#$%^&*()_+-=<>,./?}{") * amt
		txt = text
		msg = jumble + txt + jumble
		print("\r{}".format(msg), end='')
		time.sleep(wait)
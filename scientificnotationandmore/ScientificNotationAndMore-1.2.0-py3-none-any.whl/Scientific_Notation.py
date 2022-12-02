def sci_note(n, power):
    x = str(n)
    y = str(power)
    z = n*(10**power)
    print(x, '*', " 10^", y, '=', z)


def sci_note_in(number):
  """The value must be greater than 1"""
  if number >= 1 or number <= -1:
    i = 0
    while number / 10 ** i > 10:
      i += 1
    return str(number / 10 ** i) + "*" + "10^" + str(i)
  else:
    return "Value is not greater than 1"

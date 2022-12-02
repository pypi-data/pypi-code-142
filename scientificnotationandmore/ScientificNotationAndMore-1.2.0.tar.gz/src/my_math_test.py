def test(question, answer):
    ''' Both parameters should be strings. Returns a boolean '''
    a = input(str(question) + " ")
    if a == str(answer):
        return True
    else:
      return False

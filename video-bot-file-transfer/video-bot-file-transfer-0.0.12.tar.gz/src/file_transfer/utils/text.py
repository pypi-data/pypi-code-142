def read_from_file(file):
   with open(file) as f:
      return f.read()

def save_file(filename, content):
      f = open(filename, 'w')
      f.write(content)
      f.close()  
      return filename

def note(file, note):
    file2 = open(file, "a")
    file2.write(note)
    file2.close()

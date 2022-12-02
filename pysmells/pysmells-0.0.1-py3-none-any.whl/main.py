import os


# para mais de um projeto
# for file in os.listdir(os.curdir):
#     if os.path.isdir(file) and file != '.git':
#         os.system(f"pylint --msg-template='{{msg_id}}:{{msg}}' {file} >> {file}_pylint_errors.txt")
#         os.system(f"pycodestyle --statistics -qq {file} >> {file}_pep8_errors.txt")


os.system(f"pylint --msg-template='{{msg_id}}::{{msg}}' treste >> pylint_errors.txt")
# os.system(f"pycodestyle --statistics -qq treste >> pep8_errors.txt")
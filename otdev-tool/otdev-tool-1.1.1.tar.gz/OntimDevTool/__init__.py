version = "1.1.1"
auth_server = "http://192.168.12.81:8888/"
secure_access = False

if not secure_access:
    auth_server += "no_auth/"

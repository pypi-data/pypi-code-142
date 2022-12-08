from gitlab import Gitlab


def connect(cfg):
    host = cfg.get("gitlab", {}).get("host")
    apikey = cfg.get("gitlab", {}).get("apikey")
    gitlab = Gitlab(host, private_token=apikey)
    gitlab.auth()
    return gitlab

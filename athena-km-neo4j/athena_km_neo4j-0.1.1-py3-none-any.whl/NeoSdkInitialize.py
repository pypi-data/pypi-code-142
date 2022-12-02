from athena_km_neo4j.URLConstant import URLConstant


class NeoInitialize:
    def __init__(self, tm_domain):

        if tm_domain:
            URLConstant.TM_BASE_URL = tm_domain

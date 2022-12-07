import logging

logger = logging.getLogger("simpleLogger")


# Enters details to res
def insert_to_res(res, Id: str, r_type: str, c_type: str, compliance: str, description=None) -> dict:
    if compliance == '':
        compliance = None
    res.setdefault('Resource Id', []).append(Id)
    res.setdefault('Resource Type', []).append(r_type)
    res.setdefault('Compliance Type', []).append(c_type)
    res.setdefault('Compliance', []).append(compliance)
    res.setdefault('Description', []).append(description)
    return res


# extend res
def extend_res(res: dict, obj: list) -> dict:
    for ob in obj:
        if ob is None:
            continue
        res.setdefault('Resource Id', []).extend(ob['Resource Id'])
        res.setdefault('Resource Type', []).extend(ob['Resource Type'])
        res.setdefault('Compliance Type', []).extend(ob['Compliance Type'])
        res.setdefault('Compliance', []).extend(ob['Compliance'])
        res.setdefault('Description', []).extend(ob['Description'])
    return res


# returns the list of load balancers
def list_elb(self, region: str)-> list:
    logger.info(" ---Inside list_elb()")
    res = []
    client = self.session.client('elb', region_name= region)

    marker = ''
    while True:
        if marker == '' or marker is None:
            response = client.describe_load_balancers()
        else:
            response = client.describe_load_balancers(
                Marker=marker
            )
        for lb in response['LoadBalancerDescriptions']:
            res.append(lb['LoadBalancerName'])

        try:
            marker = response['NextMarker']
            if marker == '':
                break
        except KeyError:
            break

    return res
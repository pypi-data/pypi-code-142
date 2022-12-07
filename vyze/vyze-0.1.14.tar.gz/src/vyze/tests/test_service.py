from src.vyze import ServiceClient
from src.vyze.tests.test_system import service_url


def test_service__resolve_universe():
    sc = ServiceClient(service_url)
    data_id = sc.resolve_universe('data')
    assert len(data_id) > 0


def test_service__load_universe__public():
    sc = ServiceClient(service_url)
    data_univ = sc.load_universe(sc.resolve_universe('data'))
    assert len(data_univ.models) > 0
    assert data_univ['base.object']


# def test_service__load_universe__private():
#     sc = ServiceClient('http://localhost:9150')
#     sc.set_token('lx-FlBARh6kuhm0qPIIR7BBUJsXxCeIlHmQMVIAjdt0AAAAAAAAAAAAAAAAAAAAAY3q3YgAAAACAUQEA/BJ7Riz7aN_K5Wggo3dkz3InLhFo')
#     data_univ = sc.load_universe(sc.resolve_universe('private_universe'))
#     assert len(data_univ.models) > 0
#     assert data_univ['base.object']


def test_service__layer_profile():
    sc = ServiceClient(service_url)
    sc.set_token('AcTnSLTMXZeD3m9Rj8LfOVZCyGIAAAAA____fwIAYgAAADJwcm9maWxlL2U0ZjkwNTc2MzQzMjgzNWQ2Mjc0Y2NhNjQ0MzUxZjlkL2dldFRva2VuczB1bml2ZXJzZS9jNWZhY2JjOWRjYjljMzlhYzM0Yjk4OWE4ZTc1ZGU2YS9leHBvcnS5QQPEH11r1YaJrgAzRh01909Xyg')
    # univ = sc.load_universe('18ce41cfb98e0c26d5f12797782dac68')
    profile = sc.get_layer_profile('e4f905763432835d6274cca644351f9d')
    assert profile
    print(profile)

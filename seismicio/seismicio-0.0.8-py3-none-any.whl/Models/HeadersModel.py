HEADER_KEYS = (
    'tracl', 'tracr', 'fldr', 'tracf', 'ep', 'cdp', 'cdpt', 'trid',
    'nvs', 'nhs', 'duse', 'offset', 'gelev', 'selev', 'sdepth', 'gdel',
    'sdel', 'swdep', 'gwdep', 'scalel', 'scalco', 'sx', 'sy', 'gx',
    'gy', 'counit', 'wevel', 'swevel', 'sut', 'gut', 'sstat', 'gstat',
    'tstat', 'laga', 'lagb', 'delrt', 'muts', 'mute', 'ns', 'dt',
    'gain', 'igc', 'igi', 'corr', 'sfs', 'sfe', 'slen', 'styp', 'stas',
    'stae', 'tatyp', 'afilf', 'afils', 'nofilf', 'nofils', 'lcf',
    'hcf', 'lcs', 'hcs', 'year', 'day', 'hour', 'minute', 'sec',
    'timbas', 'trwf', 'grnors', 'grnofr', 'grnlof', 'gaps', 'otrav',
    'd1', 'f1', 'd2', 'f2', 'ungpow', 'unscale'
)
HEADER_KEYS_ALIASES = (
    'tracl', 'trace_record', 'fldr', 'tracf', 'ep', 'cdp', 'cdpt', 'trid',
    'nvs', 'nhs', 'duse', 'offset', 'gelev', 'selev', 'sdepth', 'gdel',
    'sdel', 'swdep', 'gwdep', 'scalel', 'scalco', 'sx', 'sy', 'gx',
    'gy', 'counit', 'wevel', 'swevel', 'sut', 'gut', 'sstat', 'gstat',
    'tstat', 'laga', 'lagb', 'delrt', 'muts', 'mute', 'ns', 'dt',
    'gain', 'igc', 'igi', 'corr', 'sfs', 'sfe', 'slen', 'styp', 'stas',
    'stae', 'tatyp', 'afilf', 'afils', 'nofilf', 'nofils', 'lcf',
    'hcf', 'lcs', 'hcs', 'year', 'day', 'hour', 'minute', 'sec',
    'timbas', 'trwf', 'grnors', 'grnofr', 'grnlof', 'gaps', 'otrav',
    'd1', 'f1', 'd2', 'f2', 'ungpow', 'unscale'
)

class Headers():
    def __init__(self):
        self.headers_dict = {}
        headers_dict = {}
        for header_key, header_key_alias in zip(HEADER_KEYS, HEADER_KEYS_ALIASES):
            headers_dict[header_key] = [0, 1, 2, 3, 4]
            self.headers_dict[header_key_alias] = headers_dict[header_key]

    def getAllHeaders(self):
        return self.headers_dict
    def getHeadersByIndex(self, index):
        # retorna dicionário {'ep': 10, 'tracf': 40}
        single_trace_headers_dict = {}
        for key, value in self.headers_dict.items():
            single_trace_headers_dict[key] = value[index]
        return single_trace_headers_dict
    def getHeadersByName(self, header_name):

        # retorna lista [30, 40, 50, 60, 70]
        return self.headers_dict[header_name]
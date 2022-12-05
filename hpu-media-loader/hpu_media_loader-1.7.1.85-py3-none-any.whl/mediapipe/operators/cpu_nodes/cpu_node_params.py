
empty_params = {}

media_constant_params = {
    'data': None,
    'layout': '',
    'shape': [1]
}

media_func_params = {
    'func': None,
    'shape': [1],
    'seed': 0,
    # 'unique_number': 0, this will be populated by framework can be used with seed to get unique seed
    'priv_params': {}  # user defined params can be passed here
}

media_ext_cpu_op_params = {
    'impl': None,
    'seed': 0,
    # 'unique_number': 0, this will be populated by framework can be used with seed to get unique seed
    'priv_params': {}  # user defined params can be passed here
}

random_biased_crop_params = {
    'patch_size': [0, 0, 0],  # do not share batch_size
    'over_sampling': 0.33,
    'num_channels': 1,
    'seed': 0,
    'num_workers': 1,
    'threshold': 0
}

basic_crop_params = {
    'patch_size': [0, 0, 0],  # do not share batch_size
    'num_channels': 1,
    'center_crop': False
}

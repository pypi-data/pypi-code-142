from .minmax import MinMaxScaler
from .standard import StandardScaler

scalers_dict = {
    'minmax01': MinMaxScaler(feature_range=(0,1)),
    'std': StandardScaler()
}
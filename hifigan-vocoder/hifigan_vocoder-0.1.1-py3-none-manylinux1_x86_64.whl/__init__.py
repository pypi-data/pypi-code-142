from pathlib import Path
import gdown
import os
import json
import torch
import numpy as np
from hifigan_vocoder.models import Generator



MODEL_URL = {
    "uni": {
        1: [
            "https://drive.google.com/file/d/1OmPeye0lOaSrXqPbAqHQRepwBJnKb5cL/view?usp=sharing",
            "https://drive.google.com/file/d/1U9Ywfl7G0KyOGIfL5fNUkSedxH3ADMMv/view?usp=sharing"
        ]
    },
    "ss": {
        1: [
            "https://drive.google.com/file/d/1pDehrRgoF1JrMdAcvR0JNYfo-UJowI2j/view?usp=sharing",
            "https://drive.google.com/file/d/1U9Ywfl7G0KyOGIfL5fNUkSedxH3ADMMv/view?usp=sharing"
        ]
    },
    "vctk": {
        1: [
            "https://drive.google.com/file/d/1yMCfqztc9Z9Q6vupOFGflDb8qAtgdlN-/view?usp=sharing",
            "https://drive.google.com/file/d/1EEhgd35zieHtTIa8k8wgn4938Kmh0iS1/view?usp=sharing"
        ]
    }
}



class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
    
        
        
class hifigan():
    def __init__(self, dataset='uni', ver=1, device='cpu'):
        self.device = torch.device(device)
        self.dataset = dataset
        self.ver = ver
        self.MAX_WAV_VALUE = 32768.0
        self.model = self.get_model()
        
    def get_model(self):
    
        if self.dataset not in MODEL_URL.keys():
            raise RuntimeError('Unsupport dataset.')
        
        model_path = str(Path(__file__).resolve().parent.joinpath(f"{self.dataset}_{self.ver}.pth"))
        config_path = str(Path(__file__).resolve().parent.joinpath(f"{self.dataset}_{self.ver}.json"))
        if not os.path.exists(model_path) or not os.path.exists(config_path):
            print("Downloading model...")
            checkpoint_url, config_url = MODEL_URL[self.dataset][self.ver]
            gdown.download(checkpoint_url, model_path, quiet=False, fuzzy=True, use_cookies=False)
            gdown.download(config_url, config_path, quiet=False, fuzzy=True, use_cookies=False)

        with open(config_path) as f:
            data = f.read()
        json_config = json.loads(data)
        h = AttrDict(json_config)
    
        
        generator = Generator(h).to(self.device)
        state_dict_g = self.load_checkpoint(model_path, self.device)
        generator.load_state_dict(state_dict_g['generator'])
        generator.eval()
        generator.remove_weight_norm()

        return generator
        
    def load_checkpoint(self, filepath, device):
        assert os.path.isfile(filepath)
        checkpoint_dict = torch.load(filepath, map_location=device)
        print("Load checkpoint success.")
        return checkpoint_dict
    
    def infer(self, mel):
        
        if isinstance(mel, np.ndarray):
            mel = torch.from_numpy(mel)
        elif isinstance(mel, torch.Tensor):
            pass
        else:
            raise RuntimeError("Mel datatype is not supported.")
            
        mel = mel.to(self.device)
        y_g_hat = self.model(mel)
        audio = y_g_hat.squeeze()
        audio = audio * self.MAX_WAV_VALUE
        audio = audio.detach().numpy()
        return audio
        

  

def get_sample_mel():
    mel = torch.load(Path(__file__).resolve().parent.joinpath("sample_mel.pt"))
    return mel
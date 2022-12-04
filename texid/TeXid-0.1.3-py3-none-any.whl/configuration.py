from transformers import RobertaConfig

class RobertaTeXidConfig(RobertaConfig):
    model_type = "roberta_texid"

    def __init__(self, model_ck="roberta-base", load_from_pretrained=False, num_classes=8, layers_use_from_last=4, method_for_layers='sum', **kwargs):
        """Constructs RobertaTeXidConfig."""
        super().__init__(**kwargs)
        self.num_classes = num_classes
        self.layers_use_from_last = layers_use_from_last
        self.method_for_layers = method_for_layers
        self.model_ck = model_ck
        self.load_from_pretrained = load_from_pretrained
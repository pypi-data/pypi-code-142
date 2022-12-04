import torch
import torch.nn as nn
from transformers import RobertaModel, PreTrainedModel
from TeXid import RobertaTeXidConfig
from transformers.models.roberta import RobertaPreTrainedModel

class RobertaClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""

    def __init__(self, config, num_classes):
        super(RobertaClassificationHead, self).__init__()
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        classifier_dropout = (
            config.classifier_dropout if config.classifier_dropout is not None else config.hidden_dropout_prob
        )
        self.dropout = nn.Dropout(classifier_dropout)
        self.out_proj = nn.Linear(config.hidden_size, num_classes)

    def forward(self, features, **kwargs):
        x = features[:, 0, :]  # take <s> token (equiv. to [CLS])
        x = self.dropout(x)
        x = self.dense(x)
        x = torch.tanh(x)
        x = self.dropout(x)
        x = self.out_proj(x)
        return x

class RobertaTeXidPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = RobertaTeXidConfig
    base_model_prefix = "roberta_texid"
    supports_gradient_checkpointing = True

    # Copied from transformers.models.bert.modeling_bert.BertPreTrainedModel._init_weights
    def _init_weights(self, module):
        """Initialize the weights"""
        if isinstance(module, nn.Linear):
            # Slightly different from the TF version which uses truncated_normal for initialization
            # cf https://github.com/pytorch/pytorch/pull/5617
            module.weight.data.normal_(mean=0.0, std=self.config.initializer_range)
            if module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.Embedding):
            module.weight.data.normal_(mean=0.0, std=self.config.initializer_range)
            if module.padding_idx is not None:
                module.weight.data[module.padding_idx].zero_()
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)

    def _set_gradient_checkpointing(self, module, value=False):
        if isinstance(module, RobertaEncoder):
            module.gradient_checkpointing = value

    def update_keys_to_ignore(self, config, del_keys_to_ignore):
        """Remove some keys from ignore list"""
        if not config.tie_word_embeddings:
            # must make a new list, or the class variable gets modified!
            self._keys_to_ignore_on_save = [k for k in self._keys_to_ignore_on_save if k not in del_keys_to_ignore]
            self._keys_to_ignore_on_load_missing = [
                k for k in self._keys_to_ignore_on_load_missing if k not in del_keys_to_ignore
            ]

class RobertaTeXid(RobertaTeXidPreTrainedModel):
    def __init__(self, config: RobertaTeXidConfig):
        super(RobertaTeXid, self).__init__(config)
        self.config = config
        if self.config.load_from_pretrained:
            self.texid_roberta = RobertaModel.from_pretrained(self.config.model_ck, config=self.config)
            self.config.load_from_pretrained = False
        else:
            self.texid_roberta = RobertaModel(self.config)
        self.classifier = RobertaClassificationHead(self.config, self.config.num_classes)
    
    def forward(self, inputs):
        outputs = self.texid_roberta(**inputs)
        list_sequence_output = outputs[2][(-1)*self.config.layers_use_from_last:]
        if self.config.method_for_layers == 'sum':
            sequence_output = torch.stack(list_sequence_output).sum(0)
        else:
            sequence_output = torch.stack(list_sequence_output).mean(0)
        logits = self.classifier(sequence_output)
        return logits
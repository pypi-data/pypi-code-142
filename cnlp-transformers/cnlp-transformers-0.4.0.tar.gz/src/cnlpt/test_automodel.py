
from transformers import (
    AutoConfig,
    AutoModel,
    AutoTokenizer,
    HfArgumentParser,
    Trainer,
    TrainingArguments,
)
from cnlpt.CnlpModelForClassification import CnlpModelForClassification, CnlpConfig
import torch
from nltk.tokenize import wordpunct_tokenize as tokenize
from cnlpt.api.temporal_rest import TemporalDocumentDataset
import numpy as np

AutoConfig.register("cnlpt", CnlpConfig)
AutoModel.register(CnlpConfig, CnlpModelForClassification)
model_name = 'tmills/clinical_tempeval_roberta-base'
# model_name = 'tmills/clinical_tempeval_pubmedbert'
config = AutoConfig.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, config=config)
model = CnlpModelForClassification.from_pretrained(model_name, cache_dir='./cache', config=config)
# state_dict = torch.load('temp/temporal/pytorch_model.bin')

print("AutoModel encoder weights: ")
print(model.encoder.encoder.layer[11].intermediate.dense.weight[0,:10])

# print("State dict encoder weights sample: ")
# print(state_dict['encoder.encoder.layer.11.intermediate.dense.weight'][0][:10])

print('***********\n\n\n')

print("Automodel classifier weights sample:")
print(model.classifiers[0].out_proj.weight[0,:10])

# print("Pytorch state dict classifier weights sample:")
# print(state_dict['classifiers.0.out_proj.weight'][0][:10])

args = ['--output_dir', 'save_run/', '--per_device_eval_batch_size', '8', '--do_predict', '--report_to', 'none']
parser = HfArgumentParser((TrainingArguments,))
training_args, = parser.parse_args_into_dataclasses(args=args)

trainer = Trainer(model=model, args=training_args, compute_metrics=None)
sent_text = 'The patient had a colonoscopy <cr> on March 16 , 2010 and a mass was found .'
print('The input sentence is %s' % (sent_text))
print('It is tokenized as %s' % (str(tokenizer.convert_ids_to_tokens(tokenizer.encode(sent_text)))))

dataset = TemporalDocumentDataset.from_instance_list([sent_text,], tokenizer)

output = trainer.predict(test_dataset=dataset)

timex_predictions = np.argmax(output.predictions[0], axis=2)
event_predictions = np.argmax(output.predictions[1], axis=2)
rel_predictions = np.argmax(output.predictions[2], axis=3)
rel_inds = np.where(rel_predictions > 0)

print(timex_predictions)
print(event_predictions)
print(rel_predictions)

print(rel_inds)

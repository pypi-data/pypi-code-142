from datasets import load_dataset
from torch.utils.data import DataLoader
from collections.abc import Mapping
import torch
from typing import List
from TeXid import SeqClassifierTokenizer

class TeXidDataLoader:
    def __init__(self, tokenizer_ck: str):
        super(TeXidDataLoader, self).__init__()
        dataset = load_dataset('csv', data_files=["data/data.csv"])['train']
        dataset = dataset.class_encode_column('Tense')
        dataset = dataset.train_test_split(test_size=0.3, stratify_by_column='Tense', seed=42)
        test_valid_dataset = dataset.pop('test')
        test_valid_dataset = test_valid_dataset.train_test_split(test_size=0.5, stratify_by_column='Tense', seed=42)
        dataset['valid'] = test_valid_dataset.pop('train')
        dataset['test'] = test_valid_dataset.pop('test')
        self.dataset = dataset
        self.tokenizer = SeqClassifierTokenizer(tokenizer_ck)

    def __collate_fn(self, examples):
        if isinstance(examples, (list, tuple)) and isinstance(examples[0], Mapping):
            encoded_inputs = {key: [example[key] for example in examples] for key in examples[0].keys()}
        input = encoded_inputs['Sentence']
        tok = self.tokenizer.tokenize(input, padding='max_length', truncation=True, max_length=20, return_tensors='pt')
        
        labels = encoded_inputs['Tense']
        tok_labels = torch.tensor(labels)
        
        tok['labels'] = tok_labels
        return tok

    def get_dataloader(self, types: List[str] = ["train", "valid", "test"]):
        res = []
        for type in types:
            res.append(
                DataLoader(self.dataset[type], batch_size=32, collate_fn=self.__collate_fn, num_workers=24)
            )
        return res

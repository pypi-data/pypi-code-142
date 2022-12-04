import torch
import torch.nn as nn
import pytorch_lightning as pl
from typing import List
from TeXid import RobertaTeXid, RobertaTeXidConfig
import torchmetrics

class LitRobertaTeXid(pl.LightningModule):
    def __init__(self, num_classes: int, model_ck: str, layers_use_from_last: int, method_for_layers: str):
        super(LitRobertaTeXid, self).__init__()
        config = RobertaTeXidConfig.from_pretrained(
            model_ck,
            layers_use_from_last=layers_use_from_last,
            method_for_layers=method_for_layers,
            num_classes=num_classes,
            load_from_pretrained=True,
            output_hidden_states=True,
        )
        self.roberta_texid = RobertaTeXid(config)
        self.num_classes = num_classes
        self.main_loss = nn.CrossEntropyLoss()
        self.train_acc = torchmetrics.Accuracy()
        self.valid_acc = torchmetrics.Accuracy()
        self.test_acc = torchmetrics.Accuracy()
        self.save_hyperparameters()

    def forward(self, batch):
        _ = batch.pop('labels')
        logits = self.roberta_texid(batch)
        return logits

    def export_model(self, path):
        self.roberta_texid.save_pretrained(path)

    def training_step(self, batch, batch_idx):
        labels = batch.pop('labels')
        logits = self.roberta_texid(batch)
        loss = self.main_loss(logits.view(-1, self.num_classes), labels.view(-1))
        self.log("train/loss", loss, on_epoch=True, on_step=False, sync_dist=True)
        preds = torch.argmax(logits, dim=-1)
        self.train_acc.update(preds, labels)
        return loss

    def training_epoch_end(self, outputs):
        self.log('train/acc_epoch', self.train_acc.compute(), on_epoch=True, sync_dist=True)
        self.train_acc.reset()

    def validation_step(self, batch, batch_idx):
        labels = batch.pop('labels')
        logits = self.roberta_texid(batch)
        loss = self.main_loss(logits.view(-1, self.num_classes), labels.view(-1))
        self.log("valid/loss", loss, on_epoch=True, on_step=False, sync_dist=True)
        preds = torch.argmax(logits, dim=-1)
        self.valid_acc.update(preds, labels)
        return loss

    def validation_epoch_end(self, outputs):
        self.log('valid/acc_epoch', self.valid_acc.compute(), on_epoch=True, sync_dist=True)
        self.valid_acc.reset()

    def test_step(self, batch, batch_idx):
        labels = batch.pop('labels')
        logits = self.roberta_texid(batch)
        preds = torch.argmax(logits, dim=-1)
        self.test_acc.update(preds, labels)
        return None
        
    def test_step_end(self, outputs):
        self.log('test/acc_epoch', self.test_acc.compute(), on_epoch=True, sync_dist=True)
        self.test_acc.reset()

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(self.parameters(), lr=5e-5)
        return optimizer
#!/usr/bin/env python3

"""
BERTAgent is a Python module for linguistic agency quantification in textual data.

"""
from typing import (
    Dict,
    Union,
)
import pandas as pd
import logging
import pathlib
import torch
import socket

from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

from . import _version

__version__ = _version.get_versions()['version']
version_full_info = _version.get_versions()


def pkg_info():
    """Provide some basic information about the package."""
    info = dict(name="bertagent")
    info.update(_version.get_versions())
    return info


dt0 = {
    "sents": [
        ["first sentence","we must adhere", "we must strive"],
        ["dummy test", "another stupid idea", "she did a brilliant job!"],
        ["just one sentence here"],
        ["This is a book."],
        ["I've been waiting for this amazing thing my whole life."],
        ["I am fed-up with waiting."],
        ["They are ridiculous"],
        ["They are amazing"],
        ["We are winners"],
        ["We are losers"],
        ["she is a hard working individual"],
        ["she is a hardly working individual"],
        ["We are motivated"],
        ["We are not so motivated"],
        ["We must win"],
        ["We'll lose"],
        ["Strive to achieve some goal"],
        ["Lazy and unmotivated"],
        ["well planned and well executed"],
        ["Everything is messy and uncoordinated"],
        ["uncoordinated activity"],
        ["coordinated activity"],
        ["unpredictible decisionmaker"],
        ["bad decisionmaker"],
        ["marvelous decisionmaker"],
        ["anti logic"],
        ["anti-logic"],
        ["i am very dissapointed with this decission"],
        ["we must fight for our rights"],
        ["this is a car it runs on gas"],
        ["I am afraid that I am sure that we will win"],
        ["I am afraid that I am sure that we will lose"],
        [""],
        ["yes"],
        ["no"],
        ["maybe"],
        ["He who would live must fight."],
        ["He who doesn’t wish to fight in this world, where permanent struggle is the law of life, has not the right to exist."],
        ["I know that fewer people are won over by the written word than by the spoken word and"],
        ["that every great movement on this earth owes its growth to great speakers and not to great writers."],
        ["We should take control and assert our position"],
        ["We should give up and say nothing"],
        ["no way"],
    ],
}

df0 = pd.DataFrame.from_dict(data=dt0)


MAX_LENGTH = 512
TOKENIZER_PARAMS = dict(
    add_special_tokens=True,
    max_length=MAX_LENGTH,
    padding="max_length",
    truncation=True,
    return_attention_mask=True,
)


class SentencesPredictor():
    def __init__(
            self,
            model_path: Union[str, pathlib.Path] = "EnchantedStardust/test0001",
            tokenizer_path: Union[str, pathlib.Path] = "EnchantedStardust/test0001",
            tokenizer_params: Dict = TOKENIZER_PARAMS,
            device: Union[str, torch.device] = "cuda",
            factor: float = 6.0,
            bias: float = -3.0,
            log0: logging.Logger = logging.getLogger('dummy'),
    ):
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_path,
            num_labels=1,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            tokenizer_path,
            do_lower_case=True,
        )
        self.tokenizer_params = tokenizer_params
        self.device = device
        self.factor = factor
        self.bias = bias
        self.log0 = log0

        self.model.to(device)
        self.model.eval()

        self.log0.info(f"{self.model.device = }")
        self.log0.info(f"{self.model.training = }")
        self.log0.info(f"{self.tokenizer = }")
        self.log0.info(f"{self.tokenizer_params = }")

    def predict(self, sentences):
        """Predict linguistic agency for list of sentences.

        Example Use
        ===========
        import pandas as pd
        from tqdm import tqdm
        tqdm.pandas()

        from bertagent import df0
        from bertagent import SentencesPredictor
        predictor = SentencesPredictor()

        df0["predict"] = df0.sents.progress_apply(predictor.predict)
        df0["BA_whole"] = df0.predict.apply(predictor.BA_whole)
        df0["BA_posit"] = df0.predict.apply(predictor.BA_posit)
        df0["BA_negat"] = df0.predict.apply(predictor.BA_negat)
        df0["BA_absol"] = df0.predict.apply(predictor.BA_absol)

        """
        batch_encodings = self.tokenizer(
            list(sentences),
            None,
            **self.tokenizer_params,
            return_tensors="pt",
        )
        self.model.eval()  # FIXME
        batch_encodings.to(self.model.device)

        # TODO: CONSIDER:
        # add here a sanity check on the character-length of a single
        # sentence.

        # with torch.inference_mode():
        with torch.no_grad():
            predictions = self.model(**batch_encodings)["logits"] \
                              .cpu().detach().numpy() * self.factor + self.bias

        predictions = predictions.ravel().tolist()
        batch_encodings.to(self.model.device)
        torch.cuda.empty_cache()  # CONSIDER DROP
        return predictions

    def BA_whole(self, x):
        """Get sentence-wise mean linguistic agency."""
        arr0 = [val for val in x]
        sum0 = sum(arr0)
        len0 = len(x)
        return sum0/len0

    def BA_posit(self, x):
        """Get sentence-wise mean linguistic agency (positive)."""
        arr0 = [val for val in x if val > 0]
        sum0 = sum(arr0)
        len0 = len(x)
        return sum0/len0

    def BA_negat(self, x):
        """Get sentence-wise mean linguistic agency (negative)."""
        arr0 = [abs(val) for val in x if val < 0]
        sum0 = sum(arr0)
        len0 = len(x)
        return sum0/len0

    def BA_absol(self, x):
        """Get sentence-wise mean linguistic agency (absolute)."""
        arr0 = [abs(val) for val in x]
        sum0 = sum(arr0)
        len0 = len(x)
        return sum0/len0


if __name__ == "__main__":
    pass

import os
import torch
import numpy as np


class ImageNetX:

    def __init__(self, filenames):
        self.filenames = filenames
        self.sample_idx = 0
        self.results = []

    def add_result(self, output):
        output = output.softmax(-1)
        top_idx_batch = output.argmax(1, keepdim=True)
        pred_batch = torch.gather(output, 1, top_idx_batch).squeeze()
        pred_batch = pred_batch.cpu().numpy()
        top_idx_batch = top_idx_batch.squeeze().cpu().numpy()
        for top_idx, pred in zip(top_idx_batch, pred_batch):
            filename = self.filenames[self.sample_idx]
            filename = os.path.basename(filename)
            self.results.append((filename, top_idx, pred))
            self.sample_idx += 1

    def get_accuracy(self, k=None):
        import imagenet_x
        import pandas as pd
        results = pd.DataFrame(self.results, columns=['file_name', 'predicted_class', 'predicted_probability'])
        results = results.set_index('file_name')

        error_type = 'class'
        which_factor = 'top'
        error_type = {
            "real_class": "is_correct_real",
            "metaclass": "is_metaclass_correct",
            "class": "is_correct",
        }[error_type]
        annotations = imagenet_x.load_annotations(
            which_factor=which_factor,
            partition='val',
            #filter_prototypes=filter_prototypes,
        )
        models = dict(misc=results)
        augmented_predictions = imagenet_x.augment_model_predictions(annotations, models)
        factors = imagenet_x.compute_factor_accuracies(
            augmented_predictions, imagenet_x.FACTORS, error_type=error_type
        )


        print(factors)
        return {}
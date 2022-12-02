from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.types import MixtureIDs


def get_total_batches(mixdb: MixtureDatabase, mixids: MixtureIDs, frames_per_batch: int) -> (int, int):
    from sonusai import SonusAIError

    frames = mixdb.total_samples(mixids) // mixdb.feature_step_samples
    total_batches = frames // frames_per_batch

    if total_batches == 0:
        raise SonusAIError(
            f'Error: dataset only contains {frames} frames which is not enough to fill a batch size of '
            f'{frames_per_batch}. Either provide more data or decrease the batch size')

    return total_batches


def get_frames_per_batch(batch_size: int, timesteps: int) -> int:
    return batch_size if timesteps == 0 else batch_size * timesteps

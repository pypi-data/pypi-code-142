import numpy as np
from pyaaware import ForwardTransform
from pyaaware import InverseTransform

from sonusai.mixture.types import AudioF
from sonusai.mixture.types import AudioT


def get_next_noise(audio: AudioT, offset: int, length: int) -> AudioT:
    return np.take(audio, range(offset, offset + length), mode='wrap')


def read_audio(name: str) -> AudioT:
    import sox

    from sonusai import SonusAIError
    from sonusai import logger
    from sonusai.mixture import tokenized_expandvars
    from sonusai.mixture import BIT_DEPTH
    from sonusai.mixture import CHANNEL_COUNT
    from sonusai.mixture import SAMPLE_RATE

    expanded_name, _ = tokenized_expandvars(name)

    try:
        # Read in and convert to desired format
        inp = sox.Transformer()
        inp.set_output_format(rate=SAMPLE_RATE, bits=BIT_DEPTH, channels=CHANNEL_COUNT)
        return inp.build_array(input_filepath=expanded_name,
                               sample_rate_in=int(sox.file_info.sample_rate(expanded_name)))

    except Exception as e:
        if name != expanded_name:
            logger.error(f'Error reading {name} (expanded: {expanded_name}): {e}')
        else:
            raise SonusAIError(f'Error reading {name}: {e}')


def calculate_transform_from_audio(audio: AudioT, transform: ForwardTransform) -> AudioF:
    """ Apply forward transform to input audio data to generate transform data

    audio
        Input data [samples]
    transform
        ForwardTransform object
    """
    return transform.execute_all(audio).transpose()


def calculate_audio_from_transform(data: AudioF, transform: InverseTransform, trim: bool = True) -> AudioT:
    """ Apply inverse transform to input transform data to generate audio data

    audio
        Input data [frames, bins]
    transform
        InverseTransform object
    trim
        Removes starting samples so output waveform will be time-aligned with input waveform to the transform
    """
    audio = transform.execute_all(data.transpose())
    if trim:
        audio = audio[transform.N - transform.R:]

    return audio

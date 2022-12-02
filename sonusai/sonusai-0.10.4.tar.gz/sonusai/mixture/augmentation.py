from typing import Dict
from typing import List
from typing import Union

import numpy as np

from sonusai.mixture.types import AudioT
from sonusai.mixture.types import Augmentation
from sonusai.mixture.types import Augmentations


def get_augmentations(rules: Union[List[Dict], Dict]) -> Augmentations:
    """Generate augmentations from list of input rules."""
    from sonusai.utils import dataclass_from_dict

    processed_rules = []
    if not isinstance(rules, list):
        rules = [rules]

    for rule in rules:
        expand_rules(expanded_rules=processed_rules, rule=rule)

    processed_rules = randomize_rules(rules=processed_rules)

    augmentations = []
    for processed_rule in processed_rules:
        augmentations.append(dataclass_from_dict(Augmentation, processed_rule))

    return augmentations


def expand_rules(expanded_rules: List[Dict], rule: dict) -> None:
    """Expand rules."""
    from copy import deepcopy
    from numbers import Number

    from sonusai import SonusAIError
    from sonusai.mixture import VALID_AUGMENTATIONS

    for key, value in list(rule.items()):
        if value is None:
            del rule[key]

    # replace old 'eq' rule with new 'eq1' rule to allow both for backward compatibility
    rule = {'eq1' if key == 'eq' else key: value for key, value in rule.items()}

    for key in rule:
        if key not in VALID_AUGMENTATIONS:
            nice_list = '\n'.join([f'  {item}' for item in VALID_AUGMENTATIONS])
            raise SonusAIError(f'Invalid augmentation: {key}.\nValid augmentations are:\n{nice_list}')

        if key in ['eq1', 'eq2', 'eq3']:
            # eq must be a list of length 3 or a list of length 3 lists
            valid = True
            multiple = False
            if isinstance(rule[key], list):
                if any(isinstance(el, list) for el in rule[key]):
                    multiple = True
                    for value in rule[key]:
                        if not isinstance(value, list) or len(value) != 3:
                            valid = False
                else:
                    if len(rule[key]) != 3:
                        valid = False
            else:
                valid = False

            if not valid:
                raise SonusAIError(f'Invalid augmentation value for {key}: {rule[key]}')

            if multiple:
                for value in rule[key]:
                    expanded_rule = deepcopy(rule)
                    expanded_rule[key] = deepcopy(value)
                    expand_rules(expanded_rules, expanded_rule)
                return

        elif key in ['count', 'mixup']:
            pass

        else:
            if isinstance(rule[key], list):
                for value in rule[key]:
                    if isinstance(value, list):
                        raise SonusAIError(f'Invalid augmentation value for {key}: {rule[key]}')
                    expanded_rule = deepcopy(rule)
                    expanded_rule[key] = deepcopy(value)
                    expand_rules(expanded_rules, expanded_rule)
                return
            elif not isinstance(rule[key], Number):
                if not rule[key].startswith('rand'):
                    raise SonusAIError(f'Invalid augmentation value for {key}: {rule[key]}')

    expanded_rules.append(rule)


def randomize_rules(rules: List[Dict]) -> List[Dict]:
    """Randomize rules."""
    out_rules = []
    for in_rule in rules:
        if rule_has_rand(in_rule):
            count = 1
            if 'count' in in_rule and in_rule['count'] is not None:
                count = in_rule['count']
                del in_rule['count']
            for i in range(count):
                out_rules.append(generate_random_rule(in_rule))
        else:
            out_rules.append(in_rule)
    return out_rules


def generate_random_rule(rule: dict) -> dict:
    """Generate a new rule from a rule that contains 'rand' directives."""
    from copy import deepcopy

    out_rule = deepcopy(rule)
    for key in out_rule:
        out_rule[key] = evaluate_random_rule(str(out_rule[key]))

        # convert eq values from strings to numbers
        if key in ['eq1', 'eq2', 'eq3']:
            for n in range(3):
                if isinstance(out_rule[key][n], str):
                    out_rule[key][n] = eval(out_rule[key][n])

    return out_rule


def rule_has_rand(rule: dict) -> bool:
    """Determine if any keys in the given rule contain 'rand'"""
    for key in rule:
        if 'rand' in str(rule[key]):
            return True

    return False


def apply_augmentation(audio: AudioT, augmentation: Augmentation, length_common_denominator: int = 1) -> AudioT:
    """Use sox to apply augmentations to audio data."""
    import sox

    from sonusai import SonusAIError
    from sonusai.mixture import BIT_DEPTH
    from sonusai.mixture import CHANNEL_COUNT
    from sonusai.mixture import SAMPLE_RATE

    try:
        # Apply augmentations
        tfm = sox.Transformer()
        tfm.set_input_format(rate=SAMPLE_RATE, bits=BIT_DEPTH, channels=CHANNEL_COUNT)
        tfm.set_output_format(rate=SAMPLE_RATE, bits=BIT_DEPTH, channels=CHANNEL_COUNT)

        # TODO
        #  Always normalize and remove normalize from list of available augmentations
        #  Normalize to globally set level (should this be a global config parameter,
        #  or hard-coded into the script?)
        if augmentation.normalize is not None:
            tfm.norm(db_level=augmentation.normalize)

        if augmentation.gain is not None:
            tfm.gain(gain_db=augmentation.gain, normalize=False)

        if augmentation.pitch is not None:
            tfm.pitch(n_semitones=augmentation.pitch / 100)

        if augmentation.tempo is not None:
            factor = augmentation.tempo
            if abs(factor - 1.0) <= 0.1:
                tfm.stretch(factor=factor)
            else:
                tfm.tempo(factor=factor, audio_type='s')

        if augmentation.eq1 is not None:
            tfm.equalizer(frequency=augmentation.eq1[0], width_q=augmentation.eq1[1],
                          gain_db=augmentation.eq1[2])

        if augmentation.eq2 is not None:
            tfm.equalizer(frequency=augmentation.eq2[0], width_q=augmentation.eq2[1],
                          gain_db=augmentation.eq2[2])

        if augmentation.eq3 is not None:
            tfm.equalizer(frequency=augmentation.eq3[0], width_q=augmentation.eq3[1],
                          gain_db=augmentation.eq3[2])

        if augmentation.lpf is not None:
            tfm.lowpass(frequency=augmentation.lpf)

        # Create output data
        audio_out = tfm.build_array(input_array=audio, sample_rate_in=SAMPLE_RATE)

        # make sure length is multiple of length_common_denominator
        audio_out = np.pad(array=audio_out, pad_width=(0, get_pad_length(len(audio_out), length_common_denominator)))

        return audio_out
    except Exception as e:
        raise SonusAIError(f'Error applying {augmentation}: {e}')


def estimate_audio_length(audio: AudioT, augmentation: Augmentation, length_common_denominator: int = 1) -> int:
    """Estimate the length of audio after augmentation."""
    length = len(audio)

    if augmentation.tempo is not None:
        length = int(length // augmentation.tempo)

    length += get_pad_length(length, length_common_denominator)

    return length


def get_mixups(augmentations: Augmentations) -> List[int]:
    return sorted(list(set([augmentation.mixup for augmentation in augmentations])))


def get_augmentation_indices_for_mixup(augmentations: list, mixup: int) -> list:
    indices = []
    for idx, augmentation in enumerate(augmentations):
        if mixup == augmentation.mixup:
            indices.append(idx)

    return indices


def get_pad_length(length: int, length_common_denominator: int) -> int:
    mod = int(length % length_common_denominator)
    if mod:
        return length_common_denominator - mod
    return 0


def pad_audio_to_length(audio: AudioT, length: int) -> AudioT:
    return np.pad(audio, (0, length - len(audio)))


def apply_gain(audio: AudioT, gain: float) -> AudioT:
    return np.int16(np.round(np.float32(audio) * gain))


def evaluate_random_rule(rule: str) -> Union[str, float]:
    """Evaluate 'rand' directive."""
    import re
    from random import uniform

    from sonusai.mixture.constants import RAND_PATTERN

    def rand_repl(m):
        return f'{uniform(float(m.group(1)), float(m.group(4))):.2f}'

    return eval(re.sub(RAND_PATTERN, rand_repl, rule))

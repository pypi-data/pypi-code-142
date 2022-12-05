"""Bud to find the total number of DSPS repeats."""
from dkist_processing_common.models.constants import BudName
from dkist_processing_common.models.flower_pot import SpilledDirt
from dkist_processing_common.models.flower_pot import Stem
from dkist_processing_common.models.tags import StemName

from dkist_processing_vbi.parsers.vbi_l0_fits_access import VbiL0FitsAccess


class VbiDspsBase(Stem):
    """Base class for computing total number of DSPS repeats and individual DSPSNUMs."""

    def __init__(self, stem_name: str):
        super().__init__(stem_name=stem_name)
        self.metadata_key = "current_dsps_repeat"

        # Just to help pycharm get the type linting
        self.key_to_petal_dict: dict[str, int] = dict()

    @property
    def value_set(self) -> set[int]:
        """Return the unique set of discovered DSPSNUMS."""
        return set(self.key_to_petal_dict.values())

    def setter(self, fits_obj: VbiL0FitsAccess):
        """
        Set the current DSPS Repeat number.

        Parameters
        ----------
        fits_obj
            The input fits object
        Returns
        -------
        The current DSPS repeat number
        """
        if fits_obj.ip_task_type != "observe":
            return SpilledDirt

        return getattr(fits_obj, self.metadata_key)


class VbiTotalDspsRepeatsBud(VbiDspsBase):
    """The total number of DSPS repeats.

    This is different than common's `TotalDspsRepeatsBud` because it turns out the DSPSREPS header key applies to *all*
    instrument programs executed during an OP. Fortunately, VBI seems to still have the individual DSPSNUM keys
    populated in sequence. Thus we can look at the set of DSPSNUMs and use it to infer the total number of VBI DSPS
    repeats.
    """

    def __init__(self):
        super().__init__(stem_name=BudName.num_dsps_repeats.value)

    def getter(self, key: str) -> int:
        """
        Get the total number of DSPS repeats.

        This is just the number of unique DSPSNUM values.
        """
        # The number of dsps repeats is the number of unique current_dsps values
        num_dsps_repeats = len(self.value_set)

        return num_dsps_repeats


class VbiDspsRepeatNumberFlower(VbiDspsBase):
    """The current DSPS repeat.

    This is different than common's `DspsRepeatNumberFlower` because it turns out the DSPSREPS header key applies to
    *all* instrument programs executed during an OP. Fortunately, VBI seems to still have the individual DSPSNUM keys
    populated in sequence. The issue, though, is that VBI might not be the first instrument executed and there could
    thus be an offset between 1 and the start of the sequence of VBI DSPSNUMs. This Flower computes that offset so that
    the DSPSNUMs start at 1 as expected.
    """

    def __init__(self):
        super().__init__(stem_name=StemName.dsps_repeat.value)

    def getter(self, key: str) -> int:
        """
        Get the total current DSPSNUM and remove a potential offset.

        A check is also made that *all* DSPSNUMs form a set that makes sense.
        """
        value_set = self.value_set

        # The number of dsps repeats is the number of unique current_dsps values
        num_dsps_repeats = len(value_set)

        # The minimum value will be used to normalize all DSPSNUMs so the sequence starts at 1.
        min_dsps_num = min(value_set)

        # Make sure all dsps nums are represented. I.e., a dsps num isn't missing. This would cause later failure in
        # science loops.
        sorted_dsps_nums = sorted(list(value_set))
        normalized_dsps_nums = [i - min_dsps_num + 1 for i in sorted_dsps_nums]

        if normalized_dsps_nums != list(range(1, num_dsps_repeats + 1)):
            raise ValueError(
                "Set of DSPS nums is not equal to the range of values expected from the number of DSPS nums found. "
                f"Expected range(1, {num_dsps_repeats + 1}), found {sorted_dsps_nums}."
            )

        return self.key_to_petal_dict[key] - min_dsps_num + 1

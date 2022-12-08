import numpy as np
import pytest
from astropy.io import fits
from dkist_processing_common._util.scratch import WorkflowFileSystem
from dkist_processing_common.tests.conftest import FakeGQLClient

from dkist_processing_vbi.models.tags import VbiTag
from dkist_processing_vbi.parsers.vbi_l0_fits_access import VbiL0FitsAccess
from dkist_processing_vbi.tasks.process_summit_processed import GenerateL1SummitData
from dkist_processing_vbi.tests.conftest import ensure_all_inputs_used
from dkist_processing_vbi.tests.conftest import generate_214_l0_fits_frame
from dkist_processing_vbi.tests.conftest import Vbi122DarkFrames
from dkist_processing_vbi.tests.conftest import Vbi122SummitObserveFrames
from dkist_processing_vbi.tests.conftest import VbiConstantsDb

RNG = np.random.default_rng()


@pytest.fixture(scope="function")
def process_summit_processed(tmp_path, recipe_run_id, init_vbi_constants_db):
    constants_db = VbiConstantsDb(SPECTRAL_LINE="VBI TEST LINE", NUM_DSPS_REPEATS=1)
    init_vbi_constants_db(recipe_run_id, constants_db)
    with GenerateL1SummitData(
        recipe_run_id=recipe_run_id,
        workflow_name="vbi_process_summit_processed",
        workflow_version="VX.Y",
    ) as task:
        task.scratch = WorkflowFileSystem(scratch_base_path=tmp_path, recipe_run_id=recipe_run_id)
        task.num_steps = 4
        task.num_exp_per_step = 1
        ds = Vbi122SummitObserveFrames(
            array_shape=(1, 10, 10),
            num_steps=task.num_steps,
            num_exp_per_step=task.num_exp_per_step,
            num_dsps_repeats=1,
        )
        dsd = Vbi122DarkFrames(
            array_shape=(1, 10, 10),
            num_steps=task.num_steps,
            num_exp_per_step=task.num_exp_per_step,
        )
        header_generator = (d.header() for d in ds)
        dark_header_generator = (d.header() for d in dsd)
        for p in range(1, task.num_steps + 1):
            for e in range(task.num_exp_per_step):
                header = next(header_generator)
                data = np.ones((10, 10), dtype=np.float32) * p
                hdul = generate_214_l0_fits_frame(s122_header=header, data=data)
                task.fits_data_write(
                    hdu_list=hdul,
                    tags=[
                        VbiTag.input(),
                        VbiTag.task("Observe"),
                        VbiTag.spatial_step(p),
                        VbiTag.dsps_repeat(header["DKIST009"]),
                        VbiTag.frame(),
                    ],
                )
                dark_header = next(dark_header_generator)
                hdul = generate_214_l0_fits_frame(s122_header=dark_header, data=np.ones((10, 10)))
                task.fits_data_write(
                    hdu_list=hdul,
                    tags=[
                        VbiTag.input(),
                        VbiTag.task("Dark"),
                        VbiTag.frame(),
                    ],
                )
        ensure_all_inputs_used(header_generator)
        yield task
        task.scratch.purge()
        task.constants._purge()


@pytest.fixture(scope="function")
def process_summit_processed_with_aborted_last_mosaic(
    tmp_path, recipe_run_id, init_vbi_constants_db
):
    num_steps = 4
    num_exp_per_step = 3
    num_dsps_repeats = 3
    constants_db = VbiConstantsDb(
        SPECTRAL_LINE="VBI TEST LINE", NUM_DSPS_REPEATS=num_dsps_repeats - 1
    )
    init_vbi_constants_db(recipe_run_id, constants_db)
    with GenerateL1SummitData(
        recipe_run_id=recipe_run_id,
        workflow_name="vbi_process_summit_processed",
        workflow_version="VX.Y",
    ) as task:
        task.scratch = WorkflowFileSystem(scratch_base_path=tmp_path, recipe_run_id=recipe_run_id)
        ds = Vbi122SummitObserveFrames(
            array_shape=(1, 10, 10),
            num_steps=num_steps,
            num_exp_per_step=num_exp_per_step,
            num_dsps_repeats=num_dsps_repeats,
            DKIST008_value=5280,
        )
        header_generator = (d.header() for d in ds)
        for i, header in enumerate(header_generator):
            if header["DKIST009"] == num_dsps_repeats and header["VBI__004"] > num_steps - 2:
                # Skip the last 2 mosaic steps of the last repeat
                continue
            hdul = generate_214_l0_fits_frame(s122_header=header)
            task.fits_data_write(
                hdu_list=hdul,
                tags=[
                    VbiTag.input(),
                    VbiTag.frame(),
                    VbiTag.task("observe"),
                    VbiTag.dsps_repeat(header["DKIST009"]),
                    VbiTag.spatial_step(header["VBI__004"]),
                ],
            )
        yield task, num_dsps_repeats - 1, num_exp_per_step, num_steps
        task.scratch.purge()
        task.constants._purge()


def test_process_summit_data(process_summit_processed, mocker):
    """
    Given: a set of parsed input frames of summit-processed data and a GenerateL1SummitData task
    When: the task is run
    Then: the correct data-dependent L1 headers are added, an output tag is applied to each frame, and the input tag is removed
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    process_summit_processed()

    # Make sure the input tag was removed
    assert len(list(process_summit_processed.read(tags=[VbiTag.input(), VbiTag.output()]))) == 0

    for step in range(1, process_summit_processed.num_steps + 1):
        sci_access_list = list(
            process_summit_processed.fits_data_read_fits_access(
                tags=[
                    VbiTag.calibrated(),
                    VbiTag.frame(),
                    VbiTag.spatial_step(step),
                    VbiTag.stokes("I"),
                ],
                cls=VbiL0FitsAccess,
            )
        )
        assert len(sci_access_list) == process_summit_processed.num_exp_per_step
        hdu = sci_access_list[0]._hdu
        assert np.mean(hdu.data) == step
        for obj in sci_access_list:
            assert isinstance(obj._hdu, fits.CompImageHDU)
            assert obj.data.dtype == "float32"


def test_process_summit_data_with_aborted_last_mosaic(
    process_summit_processed_with_aborted_last_mosaic, mocker
):
    """
    Given: a set of parsed input frames of summit-processed data that contain an aborted mosaic
    When: the task is run
    Then: only frames from complete mosaics are pass through as "calibrated"
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    (
        task,
        expected_num_dsps_repeats,
        num_exp_per_step,
        num_steps,
    ) = process_summit_processed_with_aborted_last_mosaic
    task()

    # Make sure the input tag was removed
    assert len(list(task.read(tags=[VbiTag.input(), VbiTag.output()]))) == 0

    for step in range(1, num_steps + 1):
        files = list(
            task.read(
                tags=[
                    VbiTag.calibrated(),
                    VbiTag.frame(),
                    VbiTag.spatial_step(step),
                    VbiTag.stokes("I"),
                ]
            )
        )
        assert len(files) == num_exp_per_step * expected_num_dsps_repeats
        for filepath in files:
            assert filepath.exists()

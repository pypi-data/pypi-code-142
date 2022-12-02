import copy
import json
import os
from lib2to3.pgen2.token import OP
from typing import Dict, List, Optional, Tuple, Type

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame, concat
from sensiml.dclproj.vizualization import plot_segments


class DataSegmentV2(object):
    def __init__(
        self,
        segment_id: int,
        capture_sample_sequence_start: int,
        capture_sample_sequence_end: int,
        columns: Optional[list] = None,
        data: Optional[np.array] = None,
        session: Optional[str] = None,
        label_value: Optional[str] = None,
        uuid: Optional[str] = None,
        capture: Optional[str] = None,
        extra_metadata: Optional[dict] = None,
    ):
        self._metadata = [
            "label_value",
            "capture",
            "segment_id",
            "capture_sample_sequence_start",
            "capture_sample_sequence_end",
            "session",
            "uuid",
            "segment_length",
        ]
        self._label_value = "" if None else str(label_value)
        self._session = session
        self._segment_id = segment_id
        self._uuid = uuid
        self._capture = capture
        self._data = data
        self._columns = columns
        self._capture_sample_sequence_start = capture_sample_sequence_start
        self._capture_sample_sequence_end = capture_sample_sequence_end
        self._extra_metadata = extra_metadata

    def __repr__(self):
        return str(self.metadata)

    def copy(self):
        """Returns a deepcopy of this item

        Returns:
            DataSegmentV2: Returns a deepcopy of the current DataSegment object
        """
        return copy.deepcopy(self)

    def to_dict(self):
        tmp = self.metadata
        tmp["columns"] = self.columns
        tmp["data"] = self.data

        return tmp

    @property
    def metadata(self):
        tmp_metadata = {k: getattr(self, f"_{k}") for k in self._metadata}
        if self._extra_metadata:
            tmp_metadata.update(self._extra_metadata)

        return tmp_metadata

    @property
    def capture(self):
        return self._capture

    @property
    def segment_id(self):
        return self._segment_id

    @property
    def label_value(self):
        return self._label_value

    @property
    def uuid(self):
        return str(self._uuid)

    @property
    def has_data(self):
        if self._data is not None:
            return True

        return False

    @property
    def data(self):
        return self._data

    @property
    def segment_length(self):
        return self._capture_sample_sequence_end - self._capture_sample_sequence_start

    @property
    def _segment_length(self):
        return self.segment_length

    @property
    def columns(self):
        return self._columns

    @property
    def capture_sample_sequence_start(self):
        return self._capture_sample_sequence_start

    @property
    def capture_sample_sequence_end(self):
        return self._capture_sample_sequence_end

    @property
    def start(self):
        return self.capture_sample_sequence_start

    @property
    def end(self):
        return self.capture_sample_sequence_end

    @property
    def session(self):
        return self._session

    def to_dataframe(self):
        if self.data is None:
            return

        return DataFrame(self.data.T, columns=self.columns)

    def get_column_index(self, column):
        if self._columns is None:
            return

        return self._columns.index(column)

    def plot(self, figsize: Tuple = (30, 4), currentAxis=None, **kwargs):

        if self._data is None:
            return

        if currentAxis is None:
            plt.figure(figsize=figsize)
            currentAxis = plt.gca()

        for index, axis in enumerate(self.data):
            currentAxis.plot(axis, label=self.columns[index])

        currentAxis.set_xlim(0, self.data.shape[1])

        plt.legend(loc=0)

        return currentAxis

    def plot_spectrogram(
        self, channel: str, fft_length: int = 512, figsize: Tuple = (30, 4), **kwargs
    ):
        """Plots the spectrogram for the signal.

        Args:
            channel (str): the channel/column of sensor data to use
            fft_length (int, optional): The size of the FTT length to use when computing the spectrogram. Defaults to 512.
            figsize (Tuple, optional): the size of the figure that will be created. Defaults to (30, 4).
        """
        if self._data is None:
            return

        fig, axis = plt.subplots(figsize=figsize)

        data = axis.specgram(
            self.data[self.get_column_index(channel)], NFFT=fft_length, **kwargs
        )


class DataSegmentsV2(object):
    def __init__(self, data: Optional[list] = None):

        self._data = []

        if data:
            self._data = data

    @property
    def data(self):
        return self._data

    def __repr__(self):
        display(self.to_dataframe())
        return ""

    def __str__(self):
        return self.to_dataframe().__str__()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __add__(self, value):
        return DataSegmentsV2(self._data + value._data)

    def __getitem__(self, key):
        return self._data[key]

    def append(self, data_segment: DataSegmentV2):
        """Append a DataSegment to the current DataSegments List

        Args:
            data_segment (DataSegmentV2):
        """
        self._data.append(data_segment)

    def extend(self, data_segments: DataSegmentV2):
        """Extend the current DataSegments object with another DataSegments object

        Args:
            data_segments (DataSegmentV2):
        """

        self._data.extend(data_segments._data)

    @property
    def only_metadata(self):
        if self._data is None:
            return True

        if self._data[0].data is None:
            return True

        return False

    def to_dataframe(self, metadata_only: bool = True):
        M = []

        if not self._data:
            return None

        if self.only_metadata:
            for segment in self._data:
                M.append(segment.metadata)

            return DataFrame(M)

        for segment in self.data:
            if metadata_only:
                M.append(DataFrame([segment.metadata]))
            else:
                tmp_df = DataFrame(segment.data.T, columns=segment.columns)
                M.append(tmp_df.assign(**segment.metadata))

        return concat(M).reset_index(drop=True)

    def apply(self, func, **kwargs) -> DataFrame:
        """Apply a function to all the segments in the DataSegments object and return a DataFrame of the resulting generated features for each datasegment.

        Args:
            func (_type_): and function object which takes a DataSegment as its first input and kwargs as the following

        Returns:
            DataFrame: A DataFrame of the generated features from the applied function
        """

        feature_vectors = []
        for segment in self.data:
            tmp_df = func(segment, **kwargs)
            feature_vectors.append(tmp_df.assign(**segment["metadata"]))

        return concat(feature_vectors).reset_index(drop=True)

    def iter_dataframe(self):

        if self.only_metadata:
            for segment in self._data:
                yield DataFrame([segment["metadata"]])
        else:
            for segment in self._data:
                tmp_df = DataFrame(segment["data"].T, columns=segment["columns"])

                yield tmp_df.assign(**segment["metadata"])

    def iterrows(self):
        for index, data_segment in enumerate(self.data):
            yield (index, data_segment.to_dict())

    def to_dcli(
        self, filename: Optional[str] = None, session: Optional[str] = None
    ) -> List:
        """Creates a .dcli file describing the segment information that can be imported into the Data Capture Lab

        Args:
            filename (Optional[str], optional): The name of the file to save it to, if None no file is created.. Defaults to None.
            session (Optional[str], optional): The name of a session to use when creating the DCLI file. if None the session from the DataSegment objects are used.. Defaults to None.

        Returns:
            List: DCLI formatted segments
        """

        def get_capture_index(dcli_capture, file_name):
            for index, capture in enumerate(dcli_capture):
                if file_name == capture["file_name"]:
                    return index

            return None

        def get_session_index(sessions, session_name):
            for index, session in enumerate(sessions):
                if session_name == session["session_name"]:
                    return index

            return None

        dcli_capture = []

        for segment in self._data:

            capture_index = get_capture_index(dcli_capture, segment.capture)

            if capture_index is None:
                dcli_capture.append({"file_name": segment.capture, "sessions": []})
                capture_index = -1

            session_index = get_session_index(
                dcli_capture[capture_index]["sessions"],
                segment.session if session is None else session,
            )

            if session_index is None:
                if session is None:
                    dcli_capture[capture_index]["sessions"].extend(
                        [{"session_name": segment.session, "segments": []}]
                    )
                else:
                    dcli_capture[capture_index]["sessions"].extend(
                        [{"session_name": session, "segments": []}]
                    )

                session_index = -1

            dcli_capture[capture_index]["sessions"][session_index]["segments"].append(
                {
                    "name": "Label",
                    "value": segment.label_value,
                    "start": segment.start,
                    "end": segment.end,
                }
            )

        if filename is not None:
            print("writing dcli file to", filename)
            json.dump(dcli_capture, open(filename, "w"))

        return dcli_capture

    def to_audacity(self, rate: int = 16000) -> List:
        """Creates multiple files with the naming convention file_{capture_name}session{session_name}.txt.

        These can be imported into Audacity directly going to File->Import->Labels

        Args:
            rate (int): Audacity uses the actual time and note number of samples. Set the rate to the sample rate for the captured date. Default is 16000.
        """

        dcli = self.to_dcli()

        for capture in dcli:
            for session in capture["sessions"]:
                outfile = "file_{capture}_session_{session}.txt".format(
                    capture=capture["file_name"], session=session["session_name"]
                )
                with open(
                    outfile,
                    "w",
                ) as out:
                    for segment in session["segments"]:
                        out.write(
                            "{start_time}\t{end_time}\t{label}\n".format(
                                start_time=segment["start"] / rate,
                                end_time=segment["end"] / rate,
                                label=segment["value"],
                            )
                        )
                    print("labels written to {outfile}".format(outfile=outfile))

    @property
    def label_values(self) -> List:
        """List all the labels in the DataSegments object"""

        label_values = set()
        for segment in self._data:
            label_values.add(segment.label_value)

        return sorted(list(label_values))

    def merge_label_values(self, data_segments: dict) -> List:
        """Merges label values between to data segments.

        Args:
            data_segments (dict): The datasegment object to merge label values with

        Returns:
            List: The sorted union of the label values from both datasegments
        """

        return sorted(
            list(set(data_segments.label_values).union(set(self.label_values)))
        )

    def merge_segments(self, delta: int = 1, verbose=False):
        """Merge segments that overlap or are within delta of each other.

        Args:
            delta (int, optional): The distance between two nonoverlapping segments where they will still be merged. Defaults to 1.

        Returns:
            DataFrame: A DataFrame consisting of the merged segments
        """

        return merge_segments(self, delta=delta, verbose=verbose)

    def filter_segments(self, min_length: int = 10000):
        """Merges data segments that are within a distance delta of each other and have the same class name."""

        new_datasegments = DataSegmentsV2()

        for _, segment in enumerate(self.data):
            if segment.segment_length > min_length:
                new_datasegments.append(segment)

        print(
            "Original Segments:",
            len(self),
            "Filtered Segments:",
            len(new_datasegments),
        )

        return new_datasegments

    def remove_overlap(self, verbose: bool = False, inplace: bool = False):
        """Removes the overlap between segments by setting the segment start and
        end of overlapping segments to the same point, halfway between the overlapping edges.

        Args:
            dcl (DCLProject): A DCLProject object that is connected to the DCLI file

        Returns:
            DataSegments: A DataSegments object consisting of the merged segments
        """
        return remove_overlap(self, verbose=verbose, inplace=inplace)

    def join_segments(self, delta: Optional[int] = None, inplace: bool = False):
        """Joins adjacent segments so that there is no empty space between segments.

        Args:
            dcl (DCLProject): A DCLProject object that is connected to the DCLI file
            delta (int): Segments outside this range will not be joined. If None, all neighboring segments will be merged regardless of the distance. Default is None.

        Returns:
            DataSegments: A DataSegments object consisting of the merged segments
        """

        return join_segments(self, delta=delta, inplace=inplace)

    def plot_segments(self, capture=None, capture_name=None, labels=None):

        plot_segments(self, capture=capture, capture_name=capture_name, labels=labels)


def check_overlap(s1, s2):
    return (
        True
        if max(
            0,
            min(s1.end, s2.end) - max(s1.start, s2.start),
        )
        > 0
        else False
    )


def check_near(s1, s2, delta):
    if delta is None:
        return True

    return True if abs(s2.start - s1.end) < delta else False


def merge_segments(
    segments: DataSegmentsV2, delta: int = 10, verbose=False
) -> DataSegmentsV2:
    """Merges data segments that are within a distance delta of each other and have the same class name.

    Args:
        segments (DataFrame): A DataFrame of segments
        delta (int, optional): The distance between two nonoverlapping segments where they will still be merged. Defaults to 10.

    Returns:
        DataFrame: DataFrame containing the merged segments
    """

    seg_groups = segments.to_dataframe().groupby(["session", "capture"])

    new_segments = DataSegmentsV2()
    for key in seg_groups.groups.keys():
        if verbose:
            print("Group", key)

        segment_list = (
            seg_groups.get_group(key)
            .sort_values(by="capture_sample_sequence_start")
            .index.values.tolist()
        )
        merge_list = []

        for index, segment_index in enumerate(segment_list):

            segment = segments[segment_index]
            next_segment = None

            if len(segment_list) - 1 != index:
                next_segment = segments[segment_list[index + 1]]

            if not merge_list:
                if len(segment_list) - 1 == index:
                    new_segments.append(segment)
                    continue
                elif next_segment.label_value != segment.label_value:
                    new_segments.append(segment)
                    continue
                elif not check_near(segment, next_segment, delta) and not check_overlap(
                    segment, next_segment
                ):
                    new_segments.append(segment)
                    continue

            if (
                len(segment_list) - 1 != index
                and next_segment.label_value == segment.label_value
                and (
                    check_near(segment, next_segment, delta)
                    or check_overlap(segment, next_segment)
                )
            ):

                if not merge_list:
                    merge_list.append(index)
                merge_list.append(index + 1)

            else:
                # do merge
                if merge_list:
                    if verbose:
                        print("merging", merge_list)

                    new_segments.append(merge_segment(segments, merge_list))
                else:
                    new_segments.append(segment)

                merge_list = []

        if merge_list:
            if verbose:
                print("merging", merge_list)
            new_segments.append(merge_segment(segments, merge_list))

    print("Original Segments:", len(segments), "Merged Segments:", len(new_segments))

    return new_segments


def merge_segment(segments, merge_list):

    tmp_segment = segments[merge_list[0]].copy()

    end = tmp_segment.end

    for segment_index in merge_list:
        if end < segments[segment_index].end:
            end = segments[segment_index].end

    tmp_segment._capture_sample_sequence_end = end

    if tmp_segment.has_data:
        capature_start = tmp_segment.start
        data = np.zeros((tmp_segment.data.shape[0], end - tmp_segment.start))
        head_index = 0
        capture_head_index = capature_start
        for segment in [segments[x] for x in merge_list]:
            segment.start + head_index
            data[:, head_index : segment.end - capature_start] = segment.data[
                :, capture_head_index - segment.start : segment.end - segment.start
            ]
            head_index += segment.end - capature_start
            capture_head_index += head_index

        tmp_segment._data = data

    return tmp_segment


def remove_overlap(
    segments: DataSegmentsV2, verbose: bool = False, inplace: bool = False
) -> DataSegmentsV2:
    """Removes the overlap between segments by setting the segment start and end of
    overlapping segments to the same point, halfway between the overlapping edges."""

    if inplace:
        new_segments = segments
    else:
        new_segments = copy.deepcopy(segments)

    seg_groups = new_segments.to_dataframe().groupby(["session", "capture"])

    for key in seg_groups.groups.keys():
        if verbose:
            print("Group", key)

        segment_list = (
            seg_groups.get_group(key)
            .sort_values(by="capture_sample_sequence_start")
            .index.values.tolist()
        )

        for index, segment_index in enumerate(segment_list[:-1]):
            segment = new_segments[segment_index]
            next_segment = new_segments[segment_list[index + 1]]

            if check_overlap(segment, next_segment):
                difference = (abs((next_segment.start - segment.end)) + 1) // 2
                segment._capture_sample_sequence_end -= difference
                next_segment._capture_sample_sequence_start += difference

                if segment.has_data:
                    segment._data = segment._data[:, :-difference]
                if next_segment.has_data:
                    next_segment._data = segment._data[:, difference:]

    return new_segments


def join_segments(
    segments, delta: Optional[int] = None, inplace: bool = False
) -> DataFrame:
    """If there are any gaps between two segments, this will bring them together so there are no unlabeled regions of data."""

    print(
        "This will drop the data, use the .refresh_data API to repopulate the data table"
    )

    if inplace:
        new_segments = segments
    else:
        new_segments = copy.deepcopy(segments)

    seg_groups = new_segments.to_dataframe().groupby(["session", "capture"])

    for key in seg_groups.groups.keys():

        segment_list = (
            seg_groups.get_group(key)
            .sort_values(by="capture_sample_sequence_start")
            .index.values.tolist()
        )

        for index, segment_index in enumerate(segment_list[:-1]):
            segment = new_segments[segment_index]
            next_segment = new_segments[segment_list[index + 1]]

            if (
                not check_overlap(segment, next_segment) and True
                if delta is None
                else check_near(segment, next_segment, delta=delta)
            ):
                difference = (abs((next_segment.start - segment.end)) + 1) // 2
                segment._capture_sample_sequence_end += difference
                next_segment._capture_sample_sequence_start -= difference

        segment._data = None
        next_segment._data = None

    return new_segments


def model_results_to_datasegments(
    results: DataFrame,
    data: Optional[np.array] = None,
    capture_name: Optional[str] = None,
    session: Optional[str] = None,
):
    datasegments = DataSegmentsV2()
    for index, result in enumerate(results.to_dict(orient="records")):
        if result["capture_sample_sequence_start"] < 0:
            print("Filtering: capture_sample_sequence_start must be > 0", result)
            continue
        if (
            result["capture_sample_sequence_start"]
            > result["capture_sample_sequence_end"]
        ):
            print(
                "Filtering: capture_sample_sequence_start must be < capture_sample_sequence_end",
                result,
            )

        if data is None:
            datasegments.append(
                DataSegmentV2(
                    segment_id=index,
                    data=None,
                    session=session,
                    capture=capture_name,
                    **result,
                )
            )
        else:
            datasegments.append(
                DataSegmentV2(
                    segment_id=index,
                    columns=data.columns.to_list(),
                    data=data.values[
                        result["capture_sample_sequence_start"] : result[
                            "capture_sample_sequence_end"
                        ]
                    ].T,
                    session=session,
                    capture=capture_name,
                    **result,
                )
            )

    return datasegments


def segment_list_to_datasegments(
    labels: DataFrame, session: str = "", dcl: Optional[object] = None
):
    """Converts a DataFrame of segments into a DataSegments object

    Args:
        labels (DataFrame): A dataframe containing the segment information
        session (str, optional): The session to set the segments too. Defaults to "".
        dcl (DCLProject): A DCLProject object that is connected to the DCLI file, If this is passed in the data property of the DataSegment objects will be filled with sensor data

    Returns:
        DataSegments
    """

    if isinstance(labels, DataFrame):
        # DCL generates segments with this format ""
        if labels.columns.to_list() == [
            "File",
            "Label",
            "Start",
            "End",
            "Length",
        ]:
            label_dict = (
                labels.rename(
                    columns={
                        "File": "capture",
                        "Label": "label_value",
                        "Start": "capture_sample_sequence_start",
                        "End": "capture_sample_sequence_end",
                    },
                )
                .sort_values(by="capture")
                .to_dict(orient="records")
            )
        else:
            if "segmenter" in labels.columns.tolist():
                labels.rename({"segmenter": "session"}, axis=1, inplace=True)
            label_dict = labels.sort_values(
                by=["capture", "session", "capture_sample_sequence_start"]
            ).to_dict(orient="records")
    else:
        raise Exception("Expected DataFrame")

    data_segments = DataSegmentsV2()
    capture_name = None
    columns = None
    data = None

    for index, label in enumerate(label_dict):

        if capture_name != label["capture"]:
            if dcl:
                capture = dcl.get_capture(label["capture"])
            else:
                capture = None
            capture_name = label["capture"]

        if capture:
            data = capture.iloc[
                label["capture_sample_sequence_start"] : label[
                    "capture_sample_sequence_end"
                ]
            ].values.T
            columns = capture.columns.values.tolist()
        else:
            data = None
            columns = None

        data_segments.append(
            DataSegmentV2(
                segment_id=index,
                capture_sample_sequence_start=label["capture_sample_sequence_start"],
                capture_sample_sequence_end=label["capture_sample_sequence_end"],
                data=data,
                columns=columns,
                session=label.get("session", session),
                label_value=label["label_value"],
                capture=label["capture"],
            )
        )

    return data_segments


def audacity_to_datasegments(
    capture_name, file_path: str, session: str = "", rate: int = 16000
):
    """Converts labels exported from Audacity into a datasegment object.

    Args:
        capture_name (str): The name of the capture file to import
        file_path (DataFrame): The file path to the Audacity Label
        session (str, optional): The session to set the segments too. Defaults to "".
        rate (int): Audacity uses the actual time and note number of samples. Set the rate to the sample rate for the captured date. Default is 16000.
        data (DataFrame): The data associated with the audacity labels


    Returns:
        Datasegments
    """

    M = []
    with open(file_path, "r") as fid:
        for line in fid.readlines():
            if line[0] == "\\":
                continue
            start, end, label = line[:-1].split("\t")
            M.append([float(start), float(end), label])

    segment_list = DataFrame(
        M,
        columns=[
            "capture_sample_sequence_start",
            "capture_sample_sequence_end",
            "label_value",
        ],
    )

    segment_list["capture_sample_sequence_start"] = (
        segment_list["capture_sample_sequence_start"] * rate
    ).astype(int)
    segment_list["capture_sample_sequence_end"] = (
        segment_list["capture_sample_sequence_end"] * rate
    ).astype(int)

    segment_list["capture"] = capture_name
    segment_list["session"] = session

    return segment_list_to_datasegments(segment_list)

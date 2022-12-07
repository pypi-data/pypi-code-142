from __future__ import print_function

import json
import logging
from collections import deque
from itertools import chain
from sys import getsizeof
from sys import stderr

try:
    from reprlib import repr
except ImportError:
    pass


class Helper:
    @staticmethod
    def print_mapping_report(
        report_file, total_records: int, mapped_folio_fields, mapped_legacy_fields
    ):
        details_start = "<details><summary>Click to expand field report</summary>     \n\n"
        details_end = "</details>   \n"
        report_file.write("\n## Mapped FOLIO fields\n")
        # report_file.write(f"{blurbs[header]}\n")

        d_sorted = {k: mapped_folio_fields[k] for k in sorted(mapped_folio_fields)}
        report_file.write(details_start)

        report_file.write("FOLIO Field | Mapped | Unmapped  \n")
        report_file.write("--- | --- | ---:  \n")
        for k, v in d_sorted.items():
            unmapped = max(total_records - v[0], 0)
            mapped = v[0]
            mp = mapped / total_records if total_records else 0
            mapped_per = "{:.0%}".format(max(mp, 0))
            up = unmapped / total_records if total_records else 0
            unmapped_per = "{:.0%}".format(max(up, 0))
            report_file.write(
                f"{k} | {max(mapped, 0):,} ({mapped_per}) | {unmapped:,} ({unmapped_per}) \n"
            )
        report_file.write(details_end)

        report_file.write("\n## Mapped Legacy fields\n")
        # report_file.write(f"{blurbs[header]}\n")

        d_sorted = {k: mapped_legacy_fields[k] for k in sorted(mapped_legacy_fields)}
        report_file.write(details_start)
        report_file.write("Legacy Field | Present | Mapped | Unmapped  \n")
        report_file.write("--- | --- | --- | ---:  \n")
        for k, v in d_sorted.items():
            present = v[0]
            present_per = "{:.1%}".format(present / total_records if total_records else 0)
            unmapped = present - v[1]
            mapped = v[1]
            mp = mapped / total_records if total_records else 0
            mapped_per = "{:.0%}".format(max(mp, 0))
            report_file.write(
                f"{k} | {max(present, 0):,} ({present_per}) | {max(mapped, 0):,} "
                f"({mapped_per}) | {unmapped:,}  \n"
            )
        report_file.write(details_end)

    @staticmethod
    def log_data_issue(index_or_id, message, legacy_value):
        logging.log(26, "DATA ISSUE\t%s\t%s\t%s", index_or_id, message, legacy_value)

    @staticmethod
    def write_to_file(file, folio_record):
        """Writes record to file.

        Args:
            file (_type_): _description_
            folio_record (_type_): _description_
        """
        file.write(f"{json.dumps(folio_record)}\n")

    @staticmethod
    def sizeof_fmt(num, suffix="B"):
        for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
            if abs(num) < 1024.0:
                return f"{num:3.1f}{unit}{suffix}"
            num /= 1024.0
        return f"{num:.1f}Yi{suffix}"

    @staticmethod
    def total_size(o, handlers={}, verbose=False):
        """Returns the approximate memory footprint an object and all of its contents.

        Automatically finds the contents of the following builtin containers and
        their subclasses:  tuple, list, deque, dict, set and frozenset.
        To search other containers, add handlers to iterate over their contents:

            handlers = {SomeContainerClass: iter,
                        OtherContainerClass: OtherContainerClass.get_elements}

        """
        dict_handler = lambda d: chain.from_iterable(d.items())
        all_handlers = {
            tuple: iter,
            list: iter,
            deque: iter,
            dict: dict_handler,
            set: iter,
            frozenset: iter,
        }
        all_handlers.update(handlers)  # user handlers take precedence
        seen = set()  # track which object id's have already been seen
        default_size = getsizeof(0)  # estimate sizeof object without __sizeof__

        def sizeof(o):
            if id(o) in seen:  # do not double count the same object
                return 0
            seen.add(id(o))
            s = getsizeof(o, default_size)

            if verbose:
                print(s, type(o), repr(o), file=stderr)

            for typ, handler in all_handlers.items():
                if isinstance(o, typ):
                    s += sum(map(sizeof, handler(o)))
                    break
            return s

        return Helper.sizeof_fmt(sizeof(o))


##### Example call #####

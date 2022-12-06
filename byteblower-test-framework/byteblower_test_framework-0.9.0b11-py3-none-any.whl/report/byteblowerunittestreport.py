"""Module for unit test reporting."""
from typing import Optional  # for type hinting

from pandas import DataFrame  # for type hinting

from ..flow import Flow  # for type hinting
from .byteblowerreport import ByteBlowerReport
from .unittestreport import UnitTestReport


class ByteBlowerUnitTestReport(ByteBlowerReport):
    """Generate test report in Unit XML format."""

    _FILE_FORMAT: str = 'xml'

    __slots__ = (
        '_output_dir',
        '_filename',
        '_title',
        '_unittestreport',
    )

    def __init__(self,
                 output_dir: Optional[str] = None,
                 filename_prefix: str = 'byteblower') -> None:
        """Create a ByteBlower Unit test report generator.

        :param output_dir:
           Location to store the report file, defaults to None
           (meaning that the "current directory" will be used)
        :type output_dir: Optional[str], optional
        :param filename_prefix: Prefix for the ByteBlower report file name,
           defaults to 'byteblower'
        :type filename_prefix: str, optional
        """
        super().__init__(output_dir=output_dir,
                         filename_prefix=filename_prefix)
        self._unittestreport = UnitTestReport()

    def add_flow(self, flow: Flow) -> None:
        """Add the flow info.

        :param flow: Flow to add the information for
        :type flow: Flow
        """
        self._unittestreport.set_subtest(flow.name)
        for analyser in flow._analysers:
            if analyser.has_passed:
                self._unittestreport.add_pass(analyser.type, analyser.log)
            else:
                self._unittestreport.add_fail(analyser.type, analyser.log)

    def render(self, api_version: str, port_list: DataFrame) -> None:
        """Render the report.

        :param port_list: Configuration of the ByteBlower Ports.
        :type port_list: DataFrame
        """
        self._unittestreport.save(name=self.report_url)

    def clear(self) -> None:
        """Start with empty report contents."""
        self._unittestreport = UnitTestReport()

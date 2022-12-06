from .... import errors
from ....utils import cached_property
from . import JobWidgetBase


class SubmitJobWidget(JobWidgetBase):
    def setup(self):
        self.job.signal.register('error', self._handle_error)

    def _handle_error(self, error):
        if isinstance(error, errors.FoundDupeError):
            self.job.error('You can override the dupe check with --ignore-dupes.')

    @cached_property
    def runtime_widget(self):
        return None

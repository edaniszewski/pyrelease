
import abc

from python_releaser import log


class Stage(metaclass=abc.ABCMeta):

    def __init__(self, config):
        self.config = config

    @property
    @abc.abstractmethod
    def name(self):
        """Get the name of the pipeline stage."""

    @abc.abstractmethod
    def run(self, ctx, dry=False):
        """Run the pipeline stage."""

    def skip(self, reason):
        # fixme: should each stage print a header or something so the
        #   output is more organized?
        log.write('skipping {}: {}'.format(self.name, reason))

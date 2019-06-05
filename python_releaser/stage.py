
import abc

from python_releaser import log


class Stage(metaclass=abc.ABCMeta):

    def __init__(self, pipeline):
        self.pipeline = pipeline
        # fixme: name and cfg key should probably be different
        self.config = pipeline.cfg.get(self.name)

        self.pipeline.dry_summary.init(self.name)

    @property
    @abc.abstractmethod
    def name(self):
        """Get the name of the pipeline stage."""

    @abc.abstractmethod
    def run(self):
        """Run the pipeline stage."""

    def skip(self, reason):
        # fixme: should each stage print a header or something so the
        #   output is more organized?
        log.write('skipping {}: {}'.format(self.name, reason), l=1)

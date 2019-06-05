
from python_releaser import log, stage


class DockerStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'docker'

    def run(self):
        pass

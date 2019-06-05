
from python_releaser import log, stage


class SetupStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'setup'

    def run(self):

        # TODO:
        #   - check if the --clean flag is set
        #   - create the dist dir (either default or user specified) if it
        #     does not exist

        pass

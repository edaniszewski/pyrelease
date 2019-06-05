
from python_releaser import log, stage


class EnvStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'env'

    def run(self):

        # TODO: load environment variables that pyreleaser needs. TBD what the
        #   full set is. also, do we require them here, or just try to load them
        #   and provide some other configuration pathway where env would override

        # - GITHUB_TOKEN

        # ----- not sure if these are needed ------
        # ----- they may be managed by CI    ------
        # - PYPI_USERNAME
        # - PYPI_PASSWORD
        # - PYPI_TEST_USERNAME
        # - PYPI_TEST_PASSWORD

        pass

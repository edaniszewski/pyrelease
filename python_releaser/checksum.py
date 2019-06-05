

# https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file


from python_releaser import log, stage


class ChecksumStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'checksum'

    def run(self):
        pass

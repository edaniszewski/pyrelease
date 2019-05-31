
import subprocess
import shutil
import os

from python_releaser import log, stage


class DistributionStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'distribution'

    def run(self, ctx, dry=False):
        """"""
        print('-- config ------')
        print(self.config)



def has_python():
    # todo: generalize
    return shutil.which('python') is not None


def has_setup_py():
    return os.path.exists('./setup.py')


def sdist(formats=None):
    if not formats:
        formats = [
            'gztar',
        ]

    cmd = ['python', 'setup.py', 'sdist', '--formats={}'.format(','.join(formats))]
    log.debug('running command: "%s"', ' '.join(cmd))

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # todo: check for error
    print(result)
    print(result.stdout)
    print(result.stderr)


import os
import shutil
import subprocess

from python_releaser import log, stage


class DistributionStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'distribution'

    def run(self):
        """"""

        if not has_python():
            if self.pipeline.dry_run:
                log.dry(self.name, 'python not found', l=1)
                self.pipeline.dry_summary.incr(self.name)
                return

            log.fatal('python is not installed', l=1)

        if not has_setup_py():
            if self.pipeline.dry_run:
                log.dry(self.name, 'setup.py not found but required for distribution', l=1)
                self.pipeline.dry_summary.incr(self.name)
                return

            log.fatal('project setup.py not found', l=1)

        # todo: need to properly parse the config..
        sdist()


def has_python():
    return shutil.which('python') is not None


def has_setup_py():
    return os.path.exists('./setup.py')


def sdist(formats=None):
    if not formats:
        formats = [
            'gztar',
        ]

    cmd = ['python', 'setup.py', 'sdist', '--formats={}'.format(','.join(formats))]
    log.debug('running command: "{}"'.format(' '.join(cmd)), l=1)

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # todo: check for error


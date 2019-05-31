
import subprocess
import shutil

from python_releaser import log, stage


class GitContextStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'git context'

    def run(self, ctx, dry=False):
        pass




def bin_exists():
    # todo:
    #   - generalize for more than just git
    #   - raise stage specific errors (e.g. X not found, X not in path, ...)
    return shutil.which('git') is not None


def is_repo():
    cmd = ['git', 'rev-parse', '--is-inside-work-tree']
    log.debug('running command: "%s"', ' '.join(cmd))

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: %s', out)

    return out == 'true'


def is_clean():
    cmd = ['git', 'status', '--porcelain']
    log.debug('running command: "%s"', ' '.join(cmd))

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: %s', out)

    return out == ''


def short_commit():
    cmd = ['git', 'show', "--format='%h'", 'HEAD', '-q']
    log.debug('running command: "%s"', ' '.join(cmd))

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: %s', out)

    return str(out)


def long_commit():
    cmd = ['git', 'show', "--format='%H'", 'HEAD', '-q']
    log.debug('running command: "%s"', ' '.join(cmd))

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: %s', out)

    return out


def tag():
    cmd = ['git', 'describe', '--tags', '--abbrev=0']
    log.debug('running command: "%s"', ' '.join(cmd))

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: %s', out)
    # todo: check for error

    return out


def url():
    cmd = ['git', 'ls-remote', '--get-url']
    log.debug('running command: "%s"', ' '.join(cmd))

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: %s', out)

    return out

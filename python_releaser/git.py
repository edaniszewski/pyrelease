
import shutil
import subprocess

from python_releaser import log, stage

# The fake git context that will be used if running with
# --dry-run and pyreleaser cannot determine the context.
fake_git_ctx = {
    'long_commit': 'none',
    'short_commit': 'none',
    'tag': 'dry-run',
    'url': 'none',
}


class GitContextStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'git context'

    def run(self):
        if not bin_exists():
            if self.pipeline.dry_run:
                log.dry(self.name, 'pyreleaser requires git to be installed (https://git-scm.com/)', l=1)
                self.pipeline.dry_summary.incr(self.name)
                self.pipeline.ctx.update(fake_git_ctx)
                return

            log.fatal('pyreleaser requires git to be installed (https://git-scm.com/)', l=1)

        if not is_repo():
            if self.pipeline.dry_run:
                log.dry(self.name, 'pyreleaser running outside of git repo; using fake context for run', l=1)
                self.pipeline.dry_summary.incr(self.name)
                self.pipeline.ctx.update(fake_git_ctx)
                return

            log.fatal('pyreleaser must be run from within a git repo', l=1)

        self.pipeline.ctx.update({
            'long_commit': long_commit(),
            'short_commit': short_commit(),
            'tag': tag(),
            'url': url(),
        })

        # TODO: check that a tag exists and that it matches the package version.


def bin_exists():
    # todo:
    #   - generalize for more than just git
    #   - raise stage specific errors (e.g. X not found, X not in path, ...)
    return shutil.which('git') is not None


def is_repo():
    cmd = ['git', 'rev-parse', '--is-inside-work-tree']
    log.debug('running command: "{}"'.format(' '.join(cmd)), l=1)

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: {}'.format(out), l=1)

    return out == 'true'


def is_clean():
    cmd = ['git', 'status', '--porcelain']
    log.debug('running command: "{}"'.format(' '.join(cmd)), l=1)

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: {}'.format(out), l=1)

    return out == ''


def short_commit():
    cmd = ['git', 'show', "--format='%h'", 'HEAD', '-q']
    log.debug('running command: "{}"'.format(' '.join(cmd)), l=1)

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: {}'.format(out), l=1)

    return str(out)


def long_commit():
    cmd = ['git', 'show', "--format='%H'", 'HEAD', '-q']
    log.debug('running command: "{}"'.format(' '.join(cmd)), l=1)

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: {}'.format(out), l=1)

    return out


def tag():
    cmd = ['git', 'describe', '--tags', '--abbrev=0']
    log.debug('running command: "{}"'.format(' '.join(cmd)), l=1)

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: {}'.format(out), l=1)
    # todo: check for error

    return out


def url():
    cmd = ['git', 'ls-remote', '--get-url']
    log.debug('running command: "{}"'.format(' '.join(cmd)), l=1)

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    out = result.stdout.strip().decode('utf-8')
    log.debug('command result: {}'.format(out), l=1)

    return out

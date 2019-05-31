
from python_releaser import config, git, log, distribution, before

# The fake git context that will be used if running with
# --dry-run and pyreleaser cannot determine the context.
fake_git_ctx = {
    'long_commit': 'none',
    'short_commit': 'none',
    'tag': 'dry-run',
    'url': 'none',
}


class Pipeline:
    """"""

    def __init__(self, config_file, dry_run=False):
        self.config_file = config_file
        self.dry_run = dry_run
        self.ctx = {}

        # Track the number of errors encountered during a dry run
        # which would lead to failure during normal run.
        # todo: could make this a class so it is easier to increment
        #   errors and to generate the summary report
        self.dry_run_errors = {
            'init': 0,
        }

        # Load the pipeline configuration
        self.cfg = config.load(self.config_file)
        self.ctx['project'] = self.cfg.get('project_name')

        # Populate the context with pre-run state.
        self._build_context()

        self.stages = [
            # fixme: should stages just take a reference to the pipeline itself?
            #   this way, they can get whatever data they need, ignore what they
            #   don't need, and can update state on their own, e.g. dry run errors
            before.BeforeStage(self.cfg.get('before')),
            git.GitContextStage(None),

            distribution.DistributionStage(self.cfg.get('distribution')),
        ]

    def run(self):
        for stage in self.stages:
            stage.run(self.ctx, dry=self.dry_run)

        if self.dry_run:
            log.write('----------------------')
            log.write('summary of dry-run:')
            log.write('  init ............ %s', 'ok' if self.dry_run_errors['init'] == 0 else str(self.dry_run_errors['init']) + ' errors')

    def _register_stages(self):
        pass

    def _build_context(self):
        if not git.bin_exists():
            if self.dry_run:
                log.dry('pyreleaser requires git to be installed (https://git-scm.com/)')
                self.dry_run_errors['init'] += 1
                self.ctx.update(fake_git_ctx)
                return

            log.fatal('pyreleaser requires git to be installed (https://git-scm.com/)')

        if not git.is_repo():
            if self.dry_run:
                log.dry('pyreleaser running outside of git repo; using fake context for run')
                self.dry_run_errors['init'] += 1
                self.ctx.update(fake_git_ctx)
                return

            log.fatal('pyreleaser must be run from within a git repo')

        self.ctx.update({
            'long_commit': git.long_commit(),
            'short_commit': git.short_commit(),
            'tag': git.tag(),
            'url': git.url(),
        })

        # TODO: check that a tag exists and that it matches the package version.

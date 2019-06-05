
from python_releaser import (before, changelog, checksum, config, distribution,
                             docker, env, git, log, publish, release, semver,
                             setup, __version__)


class DryRunSummary:

    def init(self, name):
        """Initialize a new stage to track in the summary."""
        setattr(self, name, 0)

    def incr(self, name):
        """Increment the error count for a stage, if it exists."""
        val = getattr(self, name)
        setattr(self, name, val + 1)

    def print(self):
        log.write('--------------------------')
        log.write('summary of dry-run:')

        for k, v in self.__dict__.items():
            log.write('  {:.<25s}{}'.format(
                k, str(v) + ' error(s)' if v else 'ok'
            ))


class Pipeline:
    """"""

    def __init__(self, config_file, dry_run=False):
        self.config_file = config_file
        self.dry_run = dry_run
        self.ctx = {}

        self.dry_summary = DryRunSummary()

        # Load the pipeline configuration
        self.cfg = config.load(self.config_file)
        self.ctx['project'] = self.cfg.get('project_name')

        self.stages = [
            before.BeforeStage(self),
            git.GitContextStage(self),
            semver.SemVerStage(self),
            env.EnvStage(self),
            setup.SetupStage(self),
            changelog.ChangelogStage(self),
            distribution.DistributionStage(self),
            docker.DockerStage(self),
            checksum.ChecksumStage(self),
            publish.PublishStage(self),
            release.ReleaseStage(self),
        ]

        log.write('pyreleaser')
        log.write('  version:\t{}'.format(__version__))
        log.write('  project:\t{}'.format(self.ctx['project']))
        log.write('  config file:\t{}'.format(self.config_file))

    def run(self):
        log.write('starting release pipeline')
        for stage in self.stages:
            log.write('→ {}'.format(stage.name.upper()))
            stage.run()

        if self.dry_run:
            self.dry_summary.print()


import semver as sv

from python_releaser import log, stage


class SemVerStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'parse semantic version'

    def run(self):

        tag = self.pipeline.ctx['tag']

        if tag and tag[0].lower() == 'v':
            log.debug('tag begins with "v"; stripping prefix', l=1)
            tag = tag[1:]

        try:
            version = sv.parse_version_info(tag)
        except ValueError as e:
            if self.pipeline.dry_run:
                self.pipeline.dry_summary.incr(self.name)
                log.dry(self.name, 'tag "{}" is not a valid SemVer string'.format(self.pipeline.ctx['tag']), l=1)
                self.pipeline.ctx['version'] = {
                    'major': 0,
                    'minor': 0,
                    'patch': 0,
                    'prerelease': '',
                    'build': '',
                    'full': '0.0.0',
                }
                return

            else:
                log.fatal(e, l=1)

        self.pipeline.ctx['version'] = {
            'major': version.major,
            'minor': version.minor,
            'patch': version.patch,
            'prerelease': version.prerelease,
            'build': version.build,
            'full': str(version),
        }

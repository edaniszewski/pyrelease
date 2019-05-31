
import subprocess
from jinja2 import Template
from python_releaser import log, stage


class BeforeStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'pre-run hooks'

    def run(self, ctx, dry=False):
        """"""
        log.debug('%s: running', self.name)

        if not self.config:
            return self.skip('no configuration found')

        hooks = self.config.get('hooks')
        if not hooks:
            # fixme: determine if we would want to skip here or
            #   if there are other things we'd want to do.
            return self.skip('no pre-run hooks defined')

        log.debug('%s: processing %d hooks', self.name, len(hooks))
        for hook in hooks:
            tmpl = Template(hook)
            rendered_hook = tmpl.render(**ctx)

            args = rendered_hook.split()

            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # todo: trap error, write success output / error output to log somewhere

            if result.stderr:
                log.fatal('before hook failed: "%s"', hook)

        log.debug('%s: complete', self.name)

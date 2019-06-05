
import subprocess

from jinja2 import Template

from python_releaser import log, stage


class BeforeStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'pre-run hooks'

    def run(self):
        """"""
        log.debug('{}: running'.format(self.name), l=1)

        if not self.config:
            return self.skip('no configuration found')

        hooks = self.config.get('hooks')
        if not hooks:
            # fixme: determine if we would want to skip here or
            #   if there are other things we'd want to do.
            return self.skip('no pre-run hooks defined')

        log.debug('{}: processing {} hooks'.format(self.name, len(hooks)), l=1)
        for hook in hooks:
            tmpl = Template(hook)
            rendered_hook = tmpl.render(**self.pipeline.ctx)

            args = rendered_hook.split()

            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # todo: trap error, write success output / error output to log somewhere

            if result.stderr:
                log.fatal('before hook failed: "{}"'.format(hook), l=1)

        log.debug('{}: complete'.format(self.name), l=1)

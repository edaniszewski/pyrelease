import os

from jinja2 import Template

from python_releaser import log, pipeline, templates


def init():
    if os.path.exists('.pyreleaser.yml') or os.path.exists('.pyreleaser.yaml'):
        log.fatal('pyreleaser configuration already exists')

    t = Template(templates.basic_config)
    rendered = t.render(
        project_name=os.path.basename(os.getcwd()),
    )

    with open('.pyreleaser.yml', 'w') as f:
        f.write(rendered)


def release(ctx):
    log.debug('release context: {}'.format(ctx))

    release_pipeline = pipeline.Pipeline(
        config_file=ctx.get('config'),
        dry_run=ctx.get('dry-run'),
    )

    release_pipeline.run()

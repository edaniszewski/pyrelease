""""""

import os
import yaml

from bison import Bison, DictOption, ListOption, Option, Scheme


def load(config_file):
    with open(config_file, 'r') as stream:
        options = yaml.safe_load(stream)
    return options


# FIXME: do we get anything by using bison? it'd probably be just as
#   effective to straight load yaml since we need to do a lot of
#   manual traversal and parsing of it anyways.

# __all__ = ['options', 'load']

# Configuration options for changelog generation.
'''
changelog:
    skip: false
    name_template: CHANGELOG
    format: markdown
    
    commits:
        sort: asc
        filters:
            exclude:
            - 'doc:'
    
    issues:
        sort: asc
        filters:
            exclude:
            - 'wip:'
            tags:
            - enhancement
            - bug
    
    prs:
        sort: asc
        filters:
            exclude:
            - 'doc:'
            tags:
            - something
'''
# changelog = Scheme(
#     Option('skip', field_type=bool),
#
#     Option('custom', field_type=str),  # allows you to specify a file w/ your own release notes
#
#     DictOption('commits', scheme=Scheme(
#         Option('sort', field_type=str, choices=('asc', 'desc')),
#         DictOption('filters', scheme=Scheme(
#             ListOption('exclude', member_type=str),
#         )),
#     )),
#
#     DictOption('issues', scheme=Scheme(
#         Option('sort', field_type=str, choices=('asc', 'desc')),
#         DictOption('filters', scheme=Scheme(
#             ListOption('exclude', member_type=str),
#             ListOption('tags', member_type=str),
#         )),
#     )),
#
#     DictOption('prs', scheme=Scheme(
#         Option('sort', field_type=str, choices=('asc', 'desc')),
#         DictOption('filters', scheme=Scheme(
#             ListOption('exclude', member_type=str),
#             ListOption('tags', member_type=str),
#         )),
#     )),
# )
#
# # Configuration options for generating checksums.
# checksum = Scheme(
#     Option('name_template', required=False, field_type=str),
#     Option('algorithm', required=False, field_type=str, choices=('md5', 'sha1', 'sha256', 'sha512'))
# )
#
# # Configuration options for Docker.
# docker = Scheme(
#     ListOption('build_flag_templates', member_type=str),
#     Option('dockerfile', field_type=str),
#     ListOption('image_templates', member_type=str),
#     Option('skip_push', field_type=str, choices=('true', 'false', 'auto')),
# )
#
# # Configuration for pre-run and post-run hooks.
# hooks = Scheme(
#     ListOption('pre', required=False, member_type=str),
#     ListOption('post', required=False, member_type=str),
# )
#
# # Configuration for generating the Python distribution archives.
# # FIXME - need to figure out what makes the most sense here..
# distribution = Scheme(
#     DictOption('sdist', required=False, scheme=Scheme(
#         # fixme: for now: bztar, gztar, tar, zip -- this is just a subset, but since
#         #   the options depend on the python version, we'll just start here.
#         #   (python setup.py sdist --help-formats)
#         ListOption('formats', required=False, member_type=str),
#
#         # see: python setup.py sdist --help
#         Option('dist_dir', required=False, default='dist', field_type=str),
#     )),
#
#     # TODO: support bdist + wheels -- this is platform specific and will take a bit
#     #   more work to do than simpler sdist
#
#     # https://stackoverflow.com/questions/6292652/what-is-the-difference-between-an-sdist-tar-gz-distribution-and-an-python-egg
#
#     # This can be: gztar, bztar, xztar, ztar, tar, zip, rpm, pkgtool, sdux, wininst, msi
#     # NOTE: this is different for different versions of python... for now, should start with a minimal
#     #   common set...
#     # ref: https://docs.python.org/3/distutils/builtdist.html
#
#     # Run checks?
#     #  twine:      twine check dist/*
#     #  setup.py:   setup.py check       <-- deprecated (use twine check)
#     #  none:
#     ListOption('checks', required=False, member_type=str),
# )
#
# # Configuration for PyPI.
# # fixme: same login credentials? different login credentials? other options?
# pypi = Scheme(
#     DictOption('test', scheme=Scheme(
#
#     )),
#     DictOption('release', scheme=Scheme(
#
#     )),
# )
#
# # Configuration options for publishing the project.
# publish = Scheme(
#     DictOption('pypi', scheme=pypi),
#     Option('skip', field_type=bool),
# )
#
# # Configuration options for generating a release for the project, e.g. for GitHub.
# release = Scheme(
#     DictOption('github', scheme=Scheme(
#         Option('owner', field_type=str),
#         Option('name', field_type=str),
#     )),
#     Option('draft', field_type=bool),
#     Option('prerelease', field_type=str, choices=('auto', 'true', 'false')),
#     Option('name_template', field_type=str),
#     Option('disable', field_type=bool),
# )
#
# # The scheme for the complete python-releaser configuration file.
# project = Scheme(
#     Option('project_name', required=False, field_type=str),
#
#     DictOption('hooks', required=False, scheme=hooks),
#     DictOption('checksum', required=False, scheme=checksum),
#     DictOption('changelog', required=False, scheme=changelog),
#     ListOption('docker', required=False, member_scheme=docker),
#     ListOption('env', required=False, member_type=str),
#     DictOption('distribution', required=False, scheme=distribution),
#     DictOption('publish', required=False, scheme=publish),
#     DictOption('release', required=False, scheme=release),
# )
#
# # The configuration options for python-releaser. Access to config data is mediated
# # through this `options` variable.
# options = Bison(project)

#
# def load(config_file):
#     options.config_name = os.path.splitext(config_file)[0]
#     options.add_config_paths(
#         '.',
#     )
#
#     options.parse(requires_cfg=True)
#     options.validate()
#     return options

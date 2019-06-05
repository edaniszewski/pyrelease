
"""
Example of Changelog config

changelog:
    skip: false
    use_file: changelog.txt

    commit:
        sort: asc
        filters:
            exclude
            - 'doc:'

    github:
        issues:
            sort: asc
            filters:
                exclude:
                - 'doc:'
                tags:
                - enhancement
        prs:
            sort: asc
            filters:
                exclude:
                - 'doc:'
                tags:
                - 'something
"""

from python_releaser import log, stage


class ChangelogStage(stage.Stage):
    """"""

    @property
    def name(self):
        return 'changelog'

    def run(self):
        pass

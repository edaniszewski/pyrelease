""""""

import logging
import argparse
import textwrap
import sys

from python_releaser import __version__, cmd, log


def main():
    parser = argparse.ArgumentParser(
        prog='pyreleaser',
        usage='pyreleaser [flags] <command>',
        formatter_class=argparse.RawTextHelpFormatter,
        description=textwrap.dedent('''
        Sane release flow for Python projects.
        
        commands:
          init               Generate a basic .pyreleaser.yml file for the project.
          release            Run the release pipeline for the current project.
        '''),
        epilog='for more details, see: https://github.com/edaniszewski/python_releaser'
    )

    # Flags
    parser.add_argument(
        '-v', '--version', action='store_true',
        help='print the version',
    )
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='run the release pipeline with debug logging',
    )
    parser.add_argument(
        '--clean', action='store_true',
        help='remove existing release/build artifacts prior to running (default: false)',
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='perform a dry run, skipping validation and artifact publishing',
    )
    parser.add_argument(
        '--config', default='.pyreleaser.yml',
        help='set the releaser configuration file (default: .pyreleaser.yml)',
    )
    parser.add_argument(
        '--dist-dir', default='pyrel', metavar='PATH',
        help='set the directory where build artifacts and temporary files will be kept'
    )
    parser.add_argument(
        '--timeout', default=None, type=int,
        help='timeout for the entire release process, in seconds (default: None)',
    )

    # Commands
    parser.add_argument(
        'command', help=argparse.SUPPRESS,
    )

    # Prior to parsing the args, make sure that some input was given to the CLI.
    # If no input was given (flags or commands), print the usage information.
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(2)

    args = parser.parse_args()

    if args.version:
        log.write_and_exit(__version__)

    if args.debug:
        log.logger.setLevel(logging.DEBUG)

    if args.command == 'init':
        log.debug('running init command')
        cmd.init()

    elif args.command == 'release':
        log.debug('running release command')
        cmd.release({
            'dry-run': args.dry_run,
            'clean': args.clean,
            'config': args.config,
            'timeout': args.timeout,
        })

    else:
        log.fatal(f'unrecognized command "{args.command}"')

    log.debug('done')


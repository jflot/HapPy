#!/usr/bin/python
# -*- coding: utf-8 -*-
# Based on Rémy Greinhofer (rgreinho) tutorial on subcommands in docopt
# https://github.com/rgreinho/docopt-subcommands-example

"""
Estimate assembly haploidy based on base depth of coverage histogram.

usage:
    HapPy [-hv] <command> [<args>...]

options:
    -h, --help                  shows the help
    -v, --version               shows the version

The subcommands are:
    depth       Compute coverage histogram.
    estimate    Finds peaks and modality, then computes scores of haploidy.
"""

from docopt import docopt
from docopt import DocoptExit

import commands


def main():
    args = docopt(__doc__, version="0.0.0", options_first=True)
    # Retrieve the command to execute.
    command_name = args.pop("<command>").capitalize()

    # Retrieve the command arguments.
    command_args = args.pop("<args>")
    if command_args is None:
        command_args = {}
    # After 'poping' '<command>' and '<args>', what is left in the args dictionary are the global arguments.
    # Retrieve the class from the 'commands' module.
    try:
        command_class = getattr(commands, command_name)
    except AttributeError:
        print("Unknown command. RTFM!.")
        raise DocoptExit()

    # Create an instance of the command.
    command = command_class(command_args, args)

    # Execute the command.
    command.execute()


if __name__ == "__main__":
    main()

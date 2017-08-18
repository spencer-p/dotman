import argparse
import actions

# Name of program
# TODO think of a good one
NAME = 'dotman'

# Create top level parser and add a subparser
parser = argparse.ArgumentParser(prog=NAME,
        description="{} manages and filters your dotfiles.".format(NAME))
subparsers = parser.add_subparsers(help='action to take', dest='action')

# Parser for add action
add_parser = subparsers.add_parser('add',
        description='moves an untracked file into your %(prog)s dotfile directory',
        help='start tracking a new file')
add_parser.add_argument('-f', '--file', nargs='+', required=True, help='files to start managing')
add_parser.add_argument('-p', '--package', required=True, help='package to add to')
add_parser.set_defaults(func=actions.add)

# Parser for update option
update_parser = subparsers.add_parser('update',
        description='runs filters and updates a given package',
        help='filter and update a package')
update_parser.add_argument('-p', '--package', help='package to filter and update')
update_parser.set_defaults(func=actions.update)

# Parse arguments
args = parser.parse_args()
if not args.action:
    parser.error(message='Missing action')
args.func(args)

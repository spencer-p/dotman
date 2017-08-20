import sys
import argparse
import actions
import config

def main():
    # Create top level parser
    parser = argparse.ArgumentParser(prog=config.NAME,
            description="{} manages and filters your dotfiles.".format(config.NAME))

    # Multiple config option
    parser.add_argument('-c', '--config', help='custom config file')

    # Create subparsers
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

    # Dummy init action
    init_parser = subparsers.add_parser('init',
            description='initializes the config file if necessary.\
            initialization happens automatically for other actions.',
            help='initialize config if necessary')
    init_parser.set_defaults(func=lambda args: None)

    # Parse arguments
    args = parser.parse_args()

    # Fail if missing an action
    if not args.action:
        parser.error(message='Missing action')

    # Initialize config
    config.initialize(args.config)

    # Call action
    return args.func(args)

if __name__ == '__main__':
    sys.exit(main())

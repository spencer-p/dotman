from pathlib import Path
import subprocess
import os
import config

# Update a package
def update(args):
    # Retrieve our packagedir and filter dir
    dot_dir = Path(config.get('dot_dir'))
    filter_dir = Path(config.get('filter_dir'))

    # Figure out which packages we're operating on
    packages = None
    if args.package:
        packages = [ dot_dir / args.package ]
    else:
        packages = [ p for p in dot_dir.iterdir() ]

    # Run the filter for each package
    # TODO catch more errors, add logging, etc
    for package in packages:

        # Make sure the package exists
        if package.exists() and (package / 'filter').exists():
            try:
                subprocess.run([ package / 'filter' ],
                    env = { 'PATH': str(filter_dir) + ':' + os.environ['PATH'] })
            except PermissionError as e:
                print('filter for "{package}" is not executable'.format(package=package.name))
                return 1


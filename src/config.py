from pathlib import Path
import configparser

# Name of program
# TODO think of a good one
NAME = 'dotman'

config = None

def initialize(custom_config_file = None):
    global config

    config_file = None
    config_dir = None

    # Use custom config file if passed
    if custom_config_file:
        config_file = Path(custom_config_file)
        config_dir = config_file.parent.resolve()

    # Otherwise detect default default
    else:
        config_dir = Path.home() / '.config' / NAME

        # Use xdg error if we have it
        try:
            from xdg.BaseDirectory import xdg_config_home
            config_dir = Path(xdg_config_home, NAME)
        except:
            # TODO log this? print an error?
            pass

        config_file = config_dir / 'config'

    # Load or create a config object if not done already
    if not config:
        # Create config object
        config = configparser.ConfigParser()

        # Try reading in the configuration
        if config_file.exists():
            config.read(config_file)

        # Otherwise write a new one
        else:
            # Write defaults
            config[NAME] = {'dot_dir': config_dir / 'etc',
                    'filter_dir': config_dir / 'filters'}

            # Create directory if needed
            if not config_dir.exists():
                config_dir.mkdir(parents=True)

            # Write to file
            with config_file.open('w') as f:
                config.write(f)

        # Make sure the directories exist
        # TODO this is not pythonic
        if not (config_dir / 'etc').exists():
            (config_dir / 'etc').mkdir()
        if not (config_dir / 'filters').exists():
            (config_dir / 'filters').mkdir()
    
    return config

def get(key):
    global config
    if not config:
        # TODO warning
        initialize()
    return config[NAME][key]

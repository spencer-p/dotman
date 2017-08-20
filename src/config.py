import os
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
        config_file = custom_config_file
        config_dir = os.path.abspath(os.path.dirname(custom_config_file))

    # Otherwise use default
    else:
        # Detect configuration directory first
        config_dir = os.path.join(os.environ['HOME'], '.config', NAME)

        # Use xdg error if we have it
        try:
            from xdg.BaseDirectory import xdg_config_home
            config_dir = os.path.join(xdg_config_home, NAME)
        except:
            # TODO log this? print an error?
            pass

        config_file = os.path.join(config_dir, 'config')

    # Load or create a config object if not done already
    if not config:
        # Create config object
        config = configparser.ConfigParser()

        # Try reading in the configuration
        if os.path.exists(config_file):
            config.read(config_file)

        # Otherwise write a new one
        else:
            # Write defaults
            config[NAME] = {'dot_dir': os.path.join(config_dir, 'etc'),
                    'filter_dir': os.path.join(config_dir, 'filters')}

            # Create directory if needed
            if not os.path.exists(config_dir):
                os.mkdir(config_dir)

            # Write to file
            with open(config_file, 'w') as f:
                config.write(f)
    
    return config

def get(key):
    global config
    if not config:
        # TODO warning
        initialize()
    return config[NAME][key]

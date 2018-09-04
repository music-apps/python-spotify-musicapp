import os
import yaml
from collections import namedtuple

from musicapp.auth import AuthMethod

Config = namedtuple('Config', ['client_id',
                               'client_secret',
                               'access_token_url',
                               'auth_url',
                               'api_version',
                               'api_url',
                               'base_url',
                               'auth_method', ])


def read_config():
    current_path = os.path.abspath(os.curdir)
    file_path = os.path.join(current_path, 'config.yaml')

    try:
        with open(file_path, mode='r', encoding='UTF-8') as file:
            config = yaml.load(file)
            config['base_url'] = f'{config["api_url"]}/{config["api_version"]}'
            auth_method = config['auth_method']
            config['auth_method'] = AuthMethod.__members__.get(auth_method)
            return Config(**config)
    except IOError as e:
        print(""" Error: couldn't find the configuration file 'config.yaml' on your current directory.
        * auth_method can be CLIENT_CREDENTIALS or AUTHORIZATION_CODE""")
        raise

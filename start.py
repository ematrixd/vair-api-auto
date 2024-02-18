#!/usr/bin/env python

import click
import configparser

from yaml import load, Loader

from LIBS.api.yaml_parser import YamlParser
from LIBS.api.api_parser import Swagger
from LIBS.api.vair import Vair

config = configparser.ConfigParser()
config.read('config.ini')
uri = config['node']['uri']
host = config['node']['host']
login = config['node']['login']
password = config['node']['password']
api = config['api']['api_doc']


def main(yaml_parser):
    Vair(yaml_parser).post()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('file_path', type=click.Path(exists=True))  
def start_yaml(file_path):
    if not config['node']['version']:
        print('Не указана версия')
        assert False
    swagger = Swagger(f'{uri}://{host}/', login, password, api)
    with open(file_path, 'r') as file:
        yml_data = load(file.read(), Loader=Loader)
        yaml_parser = YamlParser(yml_data, swagger)
        main(yaml_parser)


@cli.command()
def get_all_methods():
    swagger = Swagger(f'{uri}://{host}/', login, password, api)
    print(swagger.get_all_methods())


if __name__ == "__main__":
    cli()

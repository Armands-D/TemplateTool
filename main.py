#!/usr/bin/env python
import click
#import click_completion
import os
from distutils.dir_util import copy_tree

script_dir = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_HOME_DIR=f"{script_dir}/templates"

@click.group()
def cli():
    ...

def getTemplateNames(context, param, incomplete):
    return ["1", "2"]


@cli.command()
@click.argument('templates', nargs=-1)
def get(templates) -> None:
    for template in templates:
        copy_tree(f"{TEMPLATES_HOME_DIR}/{template}", os.getcwd())

@cli.command()
@click.argument('templates', nargs=-1)
def put(templates) -> None:
    for template in templates:
        ...

@cli.command()
@click.argument('tmp', nargs=-1, type=click.STRING, shell_complete=getTemplateNames)
def list(tmp) -> None:
    print("Templates List:")
    for d in os.listdir(TEMPLATES_HOME_DIR):print(d)

if __name__ == '__main__':
    cli()

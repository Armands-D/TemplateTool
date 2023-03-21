#!/usr/bin/env python

# BUILT-IN
import os
from distutils.dir_util import copy_tree
# DEPENDENCY
import click
script_dir = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_HOME_DIR=f"{script_dir}/templates"

def list_dir(path: str) -> None:
    for d in os.listdir(path):click.echo(d)

def checkRecursion():
    ...

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
@click.argument('templates', nargs=-1, type=click.Path(exists=True))
def put(templates) -> None:
    if len(templates) == 0:
        #TODO: Add current directory
        ...

    for template in templates:
        template_path: str = os.path.abspath(template)
        if os.path.isdir(template_path):
            click.echo(template_path)
            list_dir(template_path)
            # TODO: Fix recursion issue
            #copy_tree(f"{template_path}", f"{TEMPLATES_HOME_DIR}/{template_dir_name}")
            break
        elif os.path.isfile(template):
            break
        
        click.echo("Error: Not a directory")

@cli.command()
@click.argument('tmp', nargs=-1, type=click.STRING, shell_complete=getTemplateNames)
def list(tmp) -> None:
    print("Templates List:")
    list_dir(f"{TEMPLATES_HOME_DIR}")

if __name__ == '__main__':
    cli()


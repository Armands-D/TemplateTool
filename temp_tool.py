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
        cwd: str = os.getcwd()
        template_path : str = f"{cwd}/{template}"
        template_dir_name : str = os.path.dirname(template_path).split("/")[-1]
        if os.path.isdir(template_path):
            click.echo(template_dir_name)
            list_dir(template)
            # TODO: Fix recursion issue
            #copy_tree(f"{template_path}", f"{TEMPLATES_HOME_DIR}/{template_dir_name}")
            ...
        else:
            click.echo("Error: Not a direcotry")

@cli.command()
@click.argument('tmp', nargs=-1, type=click.STRING, shell_complete=getTemplateNames)
def list(tmp) -> None:
    print("Templates List:")
    list_dir(f"{TEMPLATES_HOME_DIR}")

if __name__ == '__main__':
    cli()


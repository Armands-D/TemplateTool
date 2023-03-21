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
    return [t for t in os.listdir(TEMPLATES_HOME_DIR)]

@cli.command()
@click.argument('templates', nargs=-1,type=click.STRING, shell_complete=getTemplateNames)
def get(templates) -> None:
    for template in templates:
        if os.path.isdir(f"{TEMPLATES_HOME_DIR}/{template}"):
            copy_tree(f"{TEMPLATES_HOME_DIR}/{template}", os.getcwd())
        else:
            click.echo(f"Error: {template} is not a directory." )

@cli.command()
@click.argument('templates', nargs=-1, type=click.Path(exists=True))
def put(templates) -> None:
    for template in templates:
        template_path: str = os.path.abspath(template)
        if os.path.isdir(template_path):
            if template_path in TEMPLATES_HOME_DIR:
                click.echo("Error: Recursive Directory")
                return
            click.echo(template_path)
            click.echo("Templates Copied:")
            list_dir(template_path)
            template_name: str = template_path.split("/")[-1]
            copy_tree(f"{template_path}", f"{TEMPLATES_HOME_DIR}/{template_name}")
            continue
        elif os.path.isfile(template):
            click.echo("TODO: No Impl")
            continue
        click.echo("Error: Not a directory")

@cli.command()
@click.argument('tmp', nargs=-1, type=click.STRING, shell_complete=getTemplateNames)
def list(tmp) -> None:
    print("Templates List:")
    list_dir(f"{TEMPLATES_HOME_DIR}")

if __name__ == '__main__':
    cli()


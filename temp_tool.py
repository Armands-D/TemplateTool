#!/usr/bin/env python

# BUILT-IN
import os
from distutils.dir_util import copy_tree
import subprocess
# DEPENDENCY
import click

script_dir = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_HOME_DIR=f"{script_dir}/templates"
TERM="alacritty"

def list_dir(path: str) -> None:
    for d in os.listdir(path):click.echo(d)

def nestedPath(path1: str, path2: str):
    cond1: bool = path1 in path2 
    cond2: bool = path2 in path1 
    return cond1 or cond2

def getTemplateNames(context, param, incomplete) -> list[str]:
    return [t for t in os.listdir(TEMPLATES_HOME_DIR)]

def getTermOption(term: str) -> str:
    # TODO: Add more terminal
    match term:
        case "alacritty":
            return "--working-directory"
        case "gnome-terminal":
            return "--working-directory"

@click.group()
def cli():
    ...

@cli.command()
@click.argument('templates', nargs=-1,type=click.STRING, shell_complete=getTemplateNames)
def edit(templates) -> None:
    for template in templates:
        template_path = f"{TEMPLATES_HOME_DIR}/{template}"
        if not os.path.isdir(template_path):
            os.makedirs(template_path)
        subprocess.Popen(
            [TERM, getTermOption(TERM), template_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )

@cli.command()
@click.argument('templates', nargs=-1,type=click.STRING, shell_complete=getTemplateNames)
def get(templates) -> None:
    for template in templates:
        template_path = f"{TEMPLATES_HOME_DIR}/{template}"
        if os.path.isdir(template_path):
            copy_tree(template_path, os.getcwd())
        else:
            click.echo(f"Error: {template} is not a directory." )

@cli.command()
@click.argument('templates', nargs=-1, type=click.Path(exists=True))
def add(templates) -> None:
    for template in templates:
        template_path: str = os.path.abspath(template)
        if os.path.isdir(template_path):
            if nestedPath(template_path, TEMPLATES_HOME_DIR):
                click.echo("Error: Recursive Directory")
                continue
            click.echo("Templates Copied:")
            list_dir(template_path)
            template_name: str = template_path.split("/")[-1]
            click.echo(template_path)
            copy_tree(f"{template_path}", f"{TEMPLATES_HOME_DIR}/{template_name}")
            continue
        elif os.path.isfile(template):
            # TODO: HANDLE
            click.echo("TODO: No Impl")
            continue
        click.echo("Error: Not a directory")

@cli.command()
def list() -> None:
    list_dir(f"{TEMPLATES_HOME_DIR}")

if __name__ == '__main__':
    cli()


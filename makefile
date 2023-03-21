SHELL:= /sbin/zsh

all: clean-venv virtual-install-pack source-rc

clean-venv:
	rm -rf venv
	rm -rf *.egg*

source-rc:
	source ~/.zshrc

virtual-install-pack: 
	virtualenv venv
	. venv/bin/activate
	pip install --editable .


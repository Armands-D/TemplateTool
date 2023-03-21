SHELL:= /sbin/zsh
COPY_FOLDER_ABS="/home/armands/Development/Project/tmp_copy_folder"
COPY_FOLDER_REL="../tmp_copy_folder"

all:
	echo "Testing PUT"
	temp_tool put $(COPY_FOLDER_ABS)
	temp_tool put $(COPY_FOLDER_REL)

refresh: clean-venv virtual-install-pack source-rc

clean-templates:
	rm a b c

clean-venv:
	rm -rf venv
	rm -rf *.egg*

source-rc:
	source ~/.zshrc

virtual-install-pack: 
	virtualenv venv
	. venv/bin/activate
	pip install --editable .


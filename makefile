SHELL:= /sbin/zsh
TEMPLATES_HOME_DIR="/home/armands/Development/Project/TemplateTool/templates"
COPY_FOLDER_ABS="/home/armands/Development/Project/tmp_copy_folder"
COPY_FOLDER_REL="../tmp_copy_folder"

all: 
	echo "Testing PUT"
	temp_tool put $(COPY_FOLDER_ABS)
	temp_tool put $(COPY_FOLDER_REL)
	ls "$(TEMPLATES_HOME_DIR)"

refresh: virtual-install-pack source-rc

clean-templates:
	rm -rf\
		"$(TEMPLATES_HOME_DIR)/a"\
		"$(TEMPLATES_HOME_DIR)/b"\
		"$(TEMPLATES_HOME_DIR)/c"\

clean-venv:
	rm -rf setup/venv
	rm -rf setup/*.egg*

source-rc:
	source ~/.zshrc

virtual-install-pack: 
	virtualenv venv
	. venv/bin/activate
	pip install --editable .

.PHONY: clean-venv

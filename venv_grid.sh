#!/bin/bash

print_message(){
echo
echo "************************************************"
echo $1
echo
}

check_and_install_virtualenv(){
virtual_evn_path=$(which virtualenv)
if [ -z $virtual_evn_path ];
then
install_virtualenv
else
print_message "virtualenv is installed"
fi
}

create_or_switch_to_virtual_environment(){
virtual_env_dir="../venv_grid"
if [ -d "$virtual_env_dir" ]
then
switch_to_virtual_env
else
make_virtual_environment
switch_to_virtual_env
install_requirement_txt
fi
}

install_virtualenv(){
print_message "installing virtualenv"
pip3 install virtualenv
}

make_virtual_environment(){
print_message "making virtual environment"
python3 -m venv ../venv_grid
}

install_requirement_txt(){
print_message "installing requirements"
pip3 install -r ./requirements/grid.txt
}

switch_to_virtual_env(){
print_message "switching to virtual environment"
pwd
source "../venv_grid/bin/activate"
}

check_and_install_virtualenv
create_or_switch_to_virtual_environment

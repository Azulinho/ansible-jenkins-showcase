#!/bin/bash
#ansible-playbook --private-key=~/.vagrant.d/insecure_private_key -u vagrant -i vagrant vagrant-jenkins.yml  -vvv
ansible-playbook -u root -i inventory.py vagrant-jenkins.yml  -vvv

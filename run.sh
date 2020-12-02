#!/bin/sh
. ./export_keys.sh
ansible-playbook aws-deploy-playbook.yaml
#install cli
pip3 install -e pycli/.
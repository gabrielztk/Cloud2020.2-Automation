#!/bin/sh
. ./export_keys.sh
ansible-playbook aws-deploy-playbook.yaml
# run cli
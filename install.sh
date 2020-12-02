#!/bin/sh
sudo apt update
sudo apt install ansible -y
pip install boto botocore boto3
ansible-galaxy collection install community.aws amazon.aws
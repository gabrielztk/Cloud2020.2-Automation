#!/bin/bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y
printf cloud | sudo psql -c "createuser -s cloud -W"
sudo psql -c "createdb -O cloud tasks"
sudo sh -c "echo listen_addresses=/'*/' | /etc/postgresql/10/main/postgresql.conf"
sudo sh -c "echo host all all 0.0.0.0/0 trust | /etc/postgresql/10/main/pg_hba.conf"
sudo ufw allow 5432/tcp
sudo systemctl restart postgresql


create postgresql user without prompt
postgresql install ansible 
https://github.com/geerlingguy/ansible-role-postgresql
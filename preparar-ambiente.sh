#!/bin/bash

sudo apt update
sudo apt -y upgrade
python3 -V
sudo apt install -y python3.11-venv
python3 -m venv venv
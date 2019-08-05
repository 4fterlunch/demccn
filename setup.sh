#!/usr/bin/env bash

BASEDIR=$(dirname "$0")

#install python stuff
sudo apt-get install python3-pip python3-virtualenv -y

#create venv
python3 -m venv $BASEDIR/demcnn_venv

#activate venv
source $BASEDIR/demcnn_venv/bin/activate

#install requirements
pip3 install -r $BASEDIR/requirements.txt

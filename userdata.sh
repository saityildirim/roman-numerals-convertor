#!/bin/bash
dnf update -y
dnf install python3 -y 
dnf install python3-pip -y
pip3 install flask
dnf install git -y
cd /home/ec2-user
mkdir templates && cd templates
wget https://raw.githubusercontent.com/saityildirim/roman-numerals-convertor/main/templates/index.html 
wget https://raw.githubusercontent.com/saityildirim/roman-numerals-convertor/main/templates/result.html
cd ..
wget https://raw.githubusercontent.com/saityildirim/roman-numerals-convertor/main/roman-numerals-converter-app.py
python3 /home/ec2-user/roman-numerals-converter-app.py
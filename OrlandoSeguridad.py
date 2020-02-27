import os
hostname="www.itmorelia.edu.mx"
red="200.33.171.0/24"

os.system("nmap -sP "+red)

computadora="200.33.171.6"
os.system("nmap -sT"+ computadora)

os.system("nmap -O "+computadora)
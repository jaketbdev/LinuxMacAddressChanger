#!/usr/bin/env python

import subprocess
from mac_address import mac_address

def changeMacAddress():
    interface = input('Interface >' )
    new_mac = input('New address>')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])





def changeMacBack():
    subprocess.call('ifconfig eth0 down', shell=True)
    subprocess.call('ifconfig eth0 hw ether ',mac_address,  shell=True)
    subprocess.call('ifconfig eth0 up', shell=True)


changeMacAddress()
